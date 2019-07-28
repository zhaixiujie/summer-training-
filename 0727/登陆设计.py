name=input("请输入您的用户名：")
if name=="方开":
    psw=input("请输入您的密码：")
    if psw=="123":
        print("欢迎管理员方开登陆")
    else:
        print("密码错误，请输入正确的密码")
elif name=="刘晨":
    psw=input("请输入您的密码：")
    if psw=="12345":
        print("欢迎管理员刘晨登陆")
    else:
        print("密码错误，请输入正确的密码")
elif name=="张旭":
    psw=input("请输入您的密码：")
    if psw=="123321":
        print("欢迎用户张旭登陆")
    else:
        print("密码错误，请输入正确的密码")
elif name=="沈章":
    psw=input("请输入您的密码：")
    if psw=="123456":
        print("欢迎用户沈章登陆")
    else:
        print("密码错误，请输入正确的密码")
elif name=="许景":
    psw=input("请输入您的密码：")
    if psw=="123456":
        print("欢迎用户许景登陆")
    else:
        print("密码错误，请输入正确的密码")
elif name.isdigit():
    print("用户名不能为数字，请输入正确的用户名")