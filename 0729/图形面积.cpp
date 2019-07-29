#include<iostream>
#include<cmath>
using namespace std;
#define PI 3.14
int triagle()
{
	int a, b, c, x, s1 = 0;
	cout << "请输入三角形的三边长：";
	cin >> a >> b >> c;
	x = a + b + c;
	s1 = sqrt(x*(x - a)*(x - b)*(x - c));
	cout << "面积：" << s1 << endl;
	return s1;
}
int circle()
{
	double r, area;
	cout << "请输入圆的半径：" << endl;
	cin >> r;
	area = PI * (r * r);
	cout << "面积：" << area << endl;
	return area;
}
int rectangle()
{
	int x, y, s3;
	cout << "长方形边长：" << endl;
	cin >> x >> y;
	s3 = x*y;
	cout << "面积：" << s3 << endl;
	return s3;
}

int main()
{
	cout << "请输入一下数字代表计算不同的图形面积：" << endl;
	cout << "1:三角形   2：圆形  3：长方形" << endl;
	int a;
	do {
		cin >> a;
		switch (a)
		{
		case 1:triagle(); break;
		case 2:circle(); break;
		case 3:rectangle(); break;
		default:cout << "输入数字不对，应在1 2 3中选取！" << endl;
			break;
		}
	} while (a != 1 && a != 2 && a != 3);
	return 0;
}