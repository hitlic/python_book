from base64 import b64encode
from hashlib import sha1
import struct


def hand_shake(conn, http_parser):               # 握手
    http_parser.reset()
    while True:                                  # 通信循环
        data_recv = conn.recv(1024)              # 接收数据
        http_parser.append(data_recv)            # 解析HTTP请求
        if http_parser.is_ok():
            break
    send_data = handshake_resp(http_parser.sec_websocket_key)
    conn.send(send_data.encode('utf-8'))


def handshake_resp(key):                         # 构造握手的HTTP响应
    magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'  # Magic String
    hashed = sha1(key.encode('utf-8') + magic_string.encode('utf-8'))
    resp_key = b64encode(hashed.digest()).strip().decode('utf-8')
    response = ["HTTP/1.1 101 Switching Protocols\r\n",
                "Upgrade: websocket\r\n",
                "Connection: Upgrade\r\n",
                f"Sec-WebSocket-Accept: {resp_key}\r\n", "\r\n"]
    return ''.join(response)


def mask_bytes(mask_key, data_len):                 # 掩码生成器
    m_len = len(mask_key)
    for i in range(data_len):
        yield mask_key[i % m_len]


class WSParser:
    def init(self, conn):
        self.__dict__ = dict()
        self.conn = conn

    def __byte1(self):                              # 解析第1字节
        data_1Byte = self.conn.recv(1)
        data_num = struct.unpack('>B', data_1Byte)[0]  # 字节串转数字
        self.fin = 1 if data_num & 0b10000000 == 128 else 0  # FIN(1位)
        self.opcode = data_num & 0b00001111         # opcode(5-8位)
        return data_1Byte

    def __byte2(self):                              # 解析第2字节
        data_1Byte = self.conn.recv(1)
        data_num = struct.unpack('>B', data_1Byte)[0]  # 字节串转数字
        self.massk = 1 if data_num & 0b10000000 == 128 else 0  # mask(1位)
        self.payload_len = data_num & 0b01111111    # Payload len(2-8位)
        return data_1Byte

    def __bytes_pl_ext(self):                       # 解析扩展数据长度
        if self.payload_len < 126:                  # 长度小于126
            self.payload_len_ext = None
            self.data_len = self.payload_len
            return b''
        elif self.payload_len == 126:               # 长度等于126
            data_2Bytes = self.conn.recv(2)
            self.payload_len_ext = struct.unpack(">H", data_2Bytes)[0]
            self.data_len = self.payload_len_ext
            return data_2Bytes
        else:                                       # 长度大于126
            data_8Bytes = self.conn.recv(8)
            self.payload_len_ext = struct.unpack(">Q", data_8Bytes)[0]
            self.data_len = self.payload_len_ext
            return data_8Bytes

    def __bytes_masking_key(self):                  # 解析Masking Key
        if self.massk == 1:
            data_4Bytes = self.conn.recv(4)         # 4个字节
            self.masking_key = data_4Bytes
            return data_4Bytes
        else:
            self.masking_key = None
            return b''

    def __bytes_data(self):                         # 解析数据
        data = self.conn.recv(self.data_len)
        if self.masking_key == 0:
            self.data = data.decode('utf-8')
        else:
            data_bytes = [d ^ k for d, k in         # 利用掩码解码数据
                          zip(data, mask_bytes(self.masking_key, len(data)))]
            self.data = bytearray(data_bytes).decode('utf-8')
        return data

    def parse(self):                                # 执行解析过程
        try:
            self.__byte1()
            self.__byte2()
            self.__bytes_pl_ext()
            self.__bytes_masking_key()
            self.__bytes_data()
            return True
        except Exception:
            return False


class WSBuilder:
    def init(self, conn):
        self.__dict__ = dict()
        self.conn = conn

    def __byte1(self, fin, opcode):               # 构造第1字节
        assert fin in [0, 1], 'FIN必须为0或1'
        assert 0 <= opcode <= 9, 'opcode必须为0到9的数字'
        if fin == 0:
            byte1 = struct.pack('>B', 0b00000000 | opcode)
        else:
            byte1 = struct.pack('>B', 0b10000000 | opcode)
        self.conn.send(byte1)

    def __byte2(self, masking_key, data):         # 构造第2字节
        mask = 0b10000000 if masking_key else 0
        data_len = len(data)
        payload_len = data_len if data_len < 126 else \
            (126 if data_len < 65536 else 127)
        self.conn.send(struct.pack('>B', mask | payload_len))
        self.payload_len = payload_len

    def __bytes_pl_ext(self, data):               # 构造扩展数据长度
        if self.payload_len < 126:
            return
        format_str = '>H' if self.payload_len == 126 else '>Q'
        self.conn.send(struct.pack(format_str, len(data)))

    def __bytes_masking_key(self, masking_key):   # 构造Masking key
        if masking_key is None:
            return
        assert len(masking_key) == 4, 'Masking-key为长为4的字节串！'
        self.conn.send(masking_key)

    def __bytes_data(self, text_data):            # 构造数据
        self.conn.send(text_data)

    def build(self, fin=1, opcode=1,              # 执行构造过程
              text_data=b'', masking_key=None):
        assert len(text_data) > 0, '数据不能为空！'
        self.__byte1(fin, opcode)
        self.__byte2(masking_key, text_data)
        self.__bytes_pl_ext(text_data)
        self.__bytes_masking_key(masking_key)
        self.__bytes_data(text_data)
