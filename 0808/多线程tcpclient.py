import socket
i=0
while(i<100):
    tcp_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address=("127.0.0.1",7000)
    tcp_sock.connect(address)
    tcp_sock.send(b"nice")
    data=tcp_sock.recv(1024)
    print(f"接受到的数据：{data}")
    tcp_sock.close()
    i=i+1