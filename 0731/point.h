/*20190730   类和对象   求任意3点构成的三角形面积*/
#ifndef POINT_H_
#define POINT_H_
class Point
{
	double xCoord;
	double yCoord;
public:
	Point() :xCoord(0), yCoord(0) {}//利用无参数构建函数初始化 xCoord 和 yCoord
	~Point();
	Point(double, double);
	double getxCoord();
	double getyCoord();
	//double getlenth(Point, Point);
};

class triangle
{

public:
	double L;//第一条边长
	double M;//第二条边长
	double N;//第三条边长
	//triangle() :L(0), M(0), N(0) {}
	triangle();
	~triangle();
	void getCoord(Point u[]);
	double getarea();
	double getlenth(Point, Point);
	double getslope(Point, Point);
};
#endif
