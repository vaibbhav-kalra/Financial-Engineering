#include<stdio.h>//input and output functions
#include<conio.h>//for using getch()
int main(void)//no arguments
{
	int a[10];
	int loc;
	int n,k,i;
	int ctr=0;
	for(k=0;k<=9;k++)
	{
		printf("Enter 10 values in the array:");
		scanf("%d",&a[k]);
	}
	printf("enter any number:");
	scanf("%d",&n);
	for(i=0;i<=9;i++)
	{
		if(n == a[i])
		{
			ctr=1;
			loc=i;
		}
	}
	if(ctr==1)
	{
		printf("found and the location is %d", loc);
	}
	else
	{
		printf("not found");
	}
	getch();
	//for seeing the output 
	//clrscr() is for clearing the output screen
	return 0;
}

