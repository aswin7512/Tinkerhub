import socket
def simple_server():
    host = '0.0.0.0'
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"Listening on {host}:{port}")
    conn, addr = s.accept()
    print(f"Connection from: {addr[0]}:{addr[1]}")
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received: {data}")
        conn.sendall(data.encode('utf-8'))
    conn.close()
if __name__ == "__main__" :
    simple_server()