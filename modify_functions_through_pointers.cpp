#include<stdio.h>
void modify(int *arr){
	arr[0]=99;
	arr[1]=88;
	arr[2]=77;
}
int main(){
	int a[3]={1,2,3};
	modify(a);
	printf("%d %d %d",a[0],a[1],a[2]);
}
