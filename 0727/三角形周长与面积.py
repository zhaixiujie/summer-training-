input_triangle1=int(input("请输入三角形第一条边的边长:"))
input_triangle2=int(input("请输入三角形第一条边的边长:"))
input_triangle3=int(input("请输入三角形第一条边的边长:"))
p=(input_triangle1+input_triangle2+input_triangle3)/2
if input_triangle1+input_triangle2<=input_triangle3:
    print("无法构成一个三角形")
elif input_triangle1+input_triangle3<=input_triangle2:
    print("无法构成一个三角形")
elif input_triangle2+input_triangle3<=input_triangle1:
    print("无法构成一个三角形")
else:
    print("三角形的周长是：",input_triangle1+input_triangle2+input_triangle3,"三角形的面积是：",(p*(p-input_triangle1)*(p-input_triangle2)*(p-input_triangle3))**0.5)
    