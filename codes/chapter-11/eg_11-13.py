from base64 import b64encode
from hashlib import sha1

def hand_shake(conn, http_parser):               # 握手
    http_parser.reset()
    while True:                                  # 通信循环
        data_recv = conn.recv(1024)              # 接收数据
        http_parser.append(data_recv)            # 解析HTTP请求
        if http_parser.is_ok(): break
    send_data = handshake_resp(http_parser.sec_websocket_key)
    conn.send(send_data.encode('utf-8'))

def handshake_resp(key):                         # 构造握手的HTTP响应
    magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11' # Magic String   
    hashed = sha1(key.encode('utf-8') + magic_string.encode('utf-8'))
    resp_key = b64encode(hashed.digest()).strip().decode('utf-8')
    response = ["HTTP/1.1 101 Switching Protocols\r\n",
                "Upgrade: websocket\r\n", 
                "Connection: Upgrade\r\n",
                f"Sec-WebSocket-Accept: {resp_key}\r\n", "\r\n"]
    return ''.join(response)