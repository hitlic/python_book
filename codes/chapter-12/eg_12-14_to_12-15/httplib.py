from urllib.parse import parse_qs

class Parser:
    def __init__(self, content=b''):
        self.reset()
        self.append(content)

    def reset(self):                            # 初始化/重置解析器
        self.__dict__ = {}
        self._buff = b''                        # 缓冲区
        self.top = b''                          # 首行内容
        self.head = b''                         # 头部内容
        self.body = b''                         # 正文内容
        self._head_ok = False                   # 头部是否接收完毕
        self.head_dict = dict()                # 头部信息字典

    def content(self):                          # 获取全部协议数据
        return b''.join([self.top, b'\r\n', self.head,
                         b'\r\n'*2, self.body]).decode('utf-8')

    def append(self, recved):                   # 添加新的数据
        if self._head_ok:
            self.body = b''.join([self.body, recved])
        else:
            self._buff = b''.join([self._buff, recved])
            if b'\r\n\r\n' in recved:
                top_head, self.body = self._buff.split(b'\r\n\r\n', 1)
                self.top, self.head = top_head.split(b'\r\n', 1)
                self._head_ok = True
                self._buff = b''
                self._parse_top()
                self._parse_head()

    def _parse_top(self):                       # 解析协议首行
        items = self.top.decode('utf-8').split(' ')
        if items[0].startswith('HTTP'):         # 响应
            self.type = 'RESPONSE'
            self.version = items[0]             # 协议版本
            self.resp_status = items[1]         # 响应状态码
            self.resp_desc = items[2]           # 响应状态描述
        else:
            self.type = 'REQUEST'
            self.req_method = items[0]          # 请求方法
            self.req_url = items[1]             # 请求URL
            self.query_string = ''
            if '?' in self.req_url:
                self.req_url, self.query_string = self.req_url.split('?')
            self.version = items[2]             # 协议版本

    def _parse_head(self):                      # 解析头部
        items = self.head.decode('utf-8').split('\r\n')
        for item in items:
            key, value = self._cut_kv(item, ':')
            if key == '':
                continue
            self.head_dict[key.strip().lower()] = value.strip()
        if 'Cookie' in self.head_dict:          # 解析cookie
            cookies = dict()
            for cookie in self.head_dict['Cookie'].split(';'):
                key, value = self._cut_kv(cookie, '=')
                if key == '':
                    continue
                cookies[key.strip()] = value.strip()
            self.head_dict['Cookie'] = cookies

    def _cut_kv(self, item, sym):
        if sym in item:
            key, value = item.split(sym, 1)
        else:
            key, value = item, True
        return key.strip(), value

    def cookie(self, key):                      # 获取cookie
        cookies = self._head_dic.get('Cookie', False)
        if not cookies:
            return False
        return cookies.get(key, False)

    def __getattr__(self, key):                 # 获取头部数据
        key = key.lower().replace('_', '-')
        return self.head_dict.get(key, False)

    def is_ok(self):                            # 数据接收是否完成
        if not self._head_ok:
            return False
        if self.type == 'REQUEST' and self.req_method == 'GET':
            return True
        if len(self.body) >= int(self.content_length):
            return True
        return False

    def req_params(self):                       # 解析请求参数
        if self.type == 'RESPONSE':
            return None
        if self.req_method == 'GET':
            return parse_qs(self.query_string)
        elif self.req_method == 'POST':
            return parse_qs(self.body.decode('utf-8'))
        return None