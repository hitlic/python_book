import struct

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
