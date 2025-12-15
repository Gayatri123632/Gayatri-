#include<stdio.h>
int main()
{
	char str[200];
	int i;
	int lower=0, upper=0, vowels=0, consonants=0, digits=0;
	printf("enter a string");
	
	fgets(str,sizeof(str),stdin);
	
	for (i=0;str[i]!='\0';i++)
	{
		if(str[i]>='a' && str[i] <= 'z')
		{	lower++;
		if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
		vowels++;
		else
		consonants++;
		}
		else if (str[i]>='A'&& str[i]<='Z')
		{
			upper++;
			
				if(str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
		vowels++;
			else
		consonants++;
		}
		else if(str[i]>='0'&&str[i]<='9')
		{
			digits++;
		}
		
	}
	printf("\nUppercase letters : %d",upper);
	printf("\nLowercase letters : %d",lower);
	printf("\nvowels            : %d",vowels);
	printf("\nconsonants        : %d",consonants);
	printf("\ndigits            : %d",digits);
	return 0;
}
