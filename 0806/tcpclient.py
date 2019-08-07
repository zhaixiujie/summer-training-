import socket
tcp_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
address=("127.0.0.1",7000) #运用的本地主机地址和7000端口号
tcp_sock.connect(address)
# 发送数据
tcp_sock.send(b"aaa")
# 接收一下数据
data=tcp_sock.recv(1024)
s=data.decode("utf-8") #接收数据时，调用recv(max)方法，一次最多发送指定的字节数
print(f"{s}") #f是格式化字符串
# 关闭连接
tcp_sock.close()
