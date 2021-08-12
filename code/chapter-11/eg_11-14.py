import struct


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
