import socket
global a,b
a=0
b=0
#新建一个tcp socket
udpSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#tcp是流协议
#绑定端口
udpSocket.bind(("0.0.0.0",7001))
print(f"bind 7001...")
#接收和发送
while True:
    # 接收用 recvfrom
    data,client_address = udpSocket.recvfrom(1024)
    print(f"从{client_address}接收到数据:{data}")
    a=a+1
    b=len(data)+b
    qw=("我累计接收到%d次数据，总的字节数为%d,此次的数据为")%(a,b)
    # 发送sentto
    udpSocket.sendto(qw.encode("utf-8")+data,client_address)
