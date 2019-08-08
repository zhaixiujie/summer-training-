import socket
import threading

def read(socket_fuwu):
    while True:

        recv_data = socket_fuwu.recv(1024)
        if recv_data:
            print(f'收到的信息：',recv_data.decode('gbk'))      #因为在window测试，所以使用gbk编码规则

def write(socket_fuwu):
        seng_data=("nice")
        if seng_data:
            socket_fuwu.send(seng_data.encode('gbk'))
        
def main():
    tcp_socket_host = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 服务器端口回收操作（释放端口）
    tcp_socket_host.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    # 2绑定端口
    tcp_socket_host.bind(('',7000))

    # 3监听  变为被动套接字
    tcp_socket_host.listen(128)    #128可以监听的最大数量，最大链接数

    # 4等待客户端连接
    while True:
        socket_fuwu,addr_client=tcp_socket_host.accept()  #accept(new_socket,addr)
        print(socket_fuwu)
        print(addr_client)
        t1=threading.Thread(target=read,args=(socket_fuwu,))
        t2=threading.Thread(target=write,args=(socket_fuwu,))
        t1.start()
        t2.start()
    


    #6服务套接字关闭
    # socket_fuwu.close()    #服务器一般不关闭   此时服务端口因为需要一直执行所以也不能关闭


if __name__ == '__main__':
    main()
