#include<iostream>
#include<string>
using namespace std;
struct SummerTrain
{
	char number[20];
	int age;
	string name;
	string address;
};
int main()
{
	SummerTrain xiu =
	{
		"P19301161",
		18,
		"����",
		"��԰6137",

	};
	cout << "ѧ�ţ�" << xiu.number << endl;
	cout << "���䣺" << xiu.age << endl;
	cout << "������" << xiu.name << endl;
	cout << "��ַ��" << xiu.address << endl;


	system("pause");
	return 0;
}