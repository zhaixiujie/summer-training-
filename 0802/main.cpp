#include<iostream>
#include"figure.h"
using namespace std;
figure::figure(double h, double w)
{
	height = h;
	width = w;
}
triangle::triangle(double h, double w) :figure(h,w)
{
	height = h;
	width = w;
}
double triangle::area()
{
	return 0.5*height*width;
}
rectangle::rectangle(double h, double w) :figure(h, w)
{
	height = h;
	width = w;
}
double rectangle::area()
{
	return height*width;
}
int main()
{
	triangle tri(2, 3);
	rectangle rec(2, 3);
	cout << "�����������" << tri.area() << endl;
	cout << "���������" << rec.area() << endl;
	return 0;
}