#include<stdio.h>
int main()
{
	int arr[5]={5,10,15,20,25};
	int *ptr=arr;
	int sum =0;
	for(int i =0;i<5;i++)
	{
		sum=sum+*(ptr+i);
	}
	printf("Sum = %d",sum);
	return 0;
}
