#include<stdio.h>
int main()
{
	int i,arr[5];
	int *ptr;
	ptr=&arr[0];
	printf("Enter The Elements");
	for(i=0;i<5;i++)
	{
		scanf("%d",ptr+i);
	}
	for(i=0;i<5;i++)
	{
		printf("%d\t",*(ptr+i));
	}
	return 0;
}
