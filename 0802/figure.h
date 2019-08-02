#ifndef FIGURE_H_
#define FIGURE_H_
class figure
{
protected:
	double height, width;
public:
	figure(double = 0, double = 0);
};
class triangle :public figure
{
public:
	double area();
	triangle(double = 0, double = 0);
};
class rectangle :public figure
{
public:
	double area();
	rectangle(double = 0, double = 0);
};
#endif