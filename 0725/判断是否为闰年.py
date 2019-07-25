input_year = int(input("请输入一个年份: "))
if (input_year  % 4) == 0:
   if (input_year  % 100) == 0:
       if (input_year  % 400) == 0:
           print(input_year ,"是闰年",type(input_year ))   # 整百年能被400整除的是闰年
       else:
           print(input_year ,"不是闰年",type(input_year ))
   else:
       print(input_year ,"是闰年",type(input_year ))       # 非整百年能被4整除的为闰年
else:
   print(input_year ,"不是闰年",type(input_year ))