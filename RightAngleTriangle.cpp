#include <stdio.h>
int isRightAngled(int a,int b,int c);
int main(void)
{
	int x,y,z;
	printf("enter lengths of 3 sides of triangle:");
	scanf("%d %d %d", &x, &y, &z);
	int flag=0 ;
	flag =isRightAngled(x,y,z);
	if(flag==0)
	{
		printf("Triangle is not right angled");
	}
	else if (flag==1)
	{
		printf("Triangle is right angled");
	}
	else
	{
		printf("Invalid input");
	}
}
int isRightAngled(int a, int b, int c)
{
	if(a<=0||b<=0||c<=0)
	return -1;
	else if((a*a==b*b + c*c)||(b*b==a*a + c*c)||(c*c==a*a + b*b))
	return 1;
	else return 0;
}
