/*20190730  ��Ͷ���  ������3�㹹�ɵ����������*/
#include<iostream>
#include"point.h"
#include <string>
#include <cmath>
using namespace std;

Point::Point(double x, double y) //���ô���������������ʼ�� xCoord �� yCoord
{
	xCoord = x;
	yCoord = y;
}
Point::~Point() //���ô���������������ʼ�� xCoord �� yCoord
{

}
double Point::getxCoord()
{
	return xCoord;
}
double Point::getyCoord()
{
	return yCoord;
}
double triangle::getlenth(Point a, Point b)//������֮�����
{
	double L = sqrt((a.getxCoord() - b.getxCoord())*(a.getxCoord() - b.getxCoord()) + (a.getyCoord() - b.getyCoord())*(a.getyCoord() - b.getyCoord()));//  ������빫ʽ : AB=��((x1-x2)^2+(y1-y2)^2)

	return L;
}
double triangle::getslope(Point a, Point b)//��б�ʣ��ж��Ƿ񹹳�һ��������
{
	double L;
	if ((a.getxCoord() - b.getxCoord()) == 0)
	{
		cout << "�㣨" << a.getxCoord() << "," << a.getyCoord() << ") �����" << "�㣨" << b.getxCoord() << "," << b.getyCoord() << ") ������Y����" << endl;
		return -1;
	}
	else
	{
		L = (a.getyCoord() - b.getyCoord()) / (a.getxCoord() - b.getxCoord());
	}

	return L;
}
//
void triangle::getCoord(Point p[]) //ȡ��Point������ p[4]�����ú��� getCoord��������ĸ��������
{
	for (int i = 0; i < 3; i++)
	{
		cout << "��" << i + 1 << "����������ǣ�" << p[i].getxCoord() << "," << p[i].getyCoord() << ")" << endl;
	}
}

triangle::triangle() :L(0), M(0), N(0)
{

}

triangle::~triangle()
{

}
double triangle::getarea() //�����
{
	double s = (L + M + N) / 2;
	double area = sqrt(s*(s - L)*(s - M)*(s - N));
	return area;
}

int main()
{
	double m = 0, n = 0;
	int tag = 0;
	Point p[3];                                        //�����޲������캯����ʼ������	
	triangle r;
	do{
		for (int i = 0; i < 3; i++)
		{
			cout << "�������" << i + 1 << "�����x������" << endl;
			cin >> m;
			cout << "�������" << i + 1 << "�����y������" << endl;
			cin >> n;
			p[i] = Point(m, n);                            //���ô��������캯�������鸳ֵ
		}
		if (r.getslope(p[0], p[1]) == r.getslope(p[2], p[1]))
		{
			tag = 1;
			cout << "������������겻���������Σ����������룡" << endl;
		}
		else
			tag = 0;
	} while (tag);

	r.getCoord(p);
	r.L = r.getlenth(p[0], p[1]);//  ������빫ʽ : AB=��((x1-x2)^2+(y1-y2)^2)
	r.M = r.getlenth(p[0], p[2]);
	r.N = r.getlenth(p[2], p[1]);
	cout << "�����������" << r.getarea() << endl;
	return 0;

}
