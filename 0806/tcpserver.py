import socket
global a,b
a=0
b=0
#新建一个tcp socket
tcp_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#tcp是流协议
#绑定端口
address=("0.0.0.0",7000) #运用的广播地址，都可以访问这个服务器
tcp_sock.bind(address)
print(f"bind{address}")
# 监听
tcp_sock.listen(10)

while True:
    #等待连接
    conn,addr=tcp_sock.accept() #accept()会等待并返回一个客户端的连接:
    print(f"{addr} connnected!" )
    # 接受客户端发来的数据
    data=conn.recv(1024)
    a=a+1
    b=len(data)+b
    if data==b"":
        conn.close()
    print(f"接收到的数据{data}")
    qw=("我累计接收到%d次数据，总的字节数为%d,此次的数据为")%(a,b)
    # 发送给客户端数据
    conn.send(qw.encode("utf-8")+data)
    
    # 断开连接
    conn.close
# tcp走的是数据报，用数据报传输，新建一个udp socket
udp_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)