/*20190730   ��Ͷ���   ������3�㹹�ɵ����������*/
#ifndef POINT_H_
#define POINT_H_
class Point
{
	double xCoord;
	double yCoord;
public:
	Point() :xCoord(0), yCoord(0) {}//�����޲�������������ʼ�� xCoord �� yCoord
	~Point();
	Point(double, double);
	double getxCoord();
	double getyCoord();
	//double getlenth(Point, Point);
};

class triangle
{

public:
	double L;//��һ���߳�
	double M;//�ڶ����߳�
	double N;//�������߳�
	//triangle() :L(0), M(0), N(0) {}
	triangle();
	~triangle();
	void getCoord(Point u[]);
	double getarea();
	double getlenth(Point, Point);
	double getslope(Point, Point);
};
#endif
