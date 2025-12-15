#include<stdio.h>

int main()
{
    char str[200];
    int i;

    fgets(str, sizeof(str), stdin);

    printf("\nLowercase to Uppercase: ");
    for(i=0; str[i]!='\0'; i++)
    {
        if(str[i]>='a' && str[i]<='z')
            printf("%c", str[i]-32);
        else
            printf("%c", str[i]);
    }

    printf("\nUppercase to Lowercase: ");
    for(i=0; str[i]!='\0'; i++)
    {
        if(str[i]>='A' && str[i]<='Z')
            printf("%c", str[i]+32);
        else
            printf("%c", str[i]);
    }

    printf("\nToggle Case: ");
    for(i=0; str[i]!='\0'; i++)
    {
        if(str[i]>='a' && str[i]<='z')
            printf("%c", str[i]-32);
        else if(str[i]>='A' && str[i]<='Z')
            printf("%c", str[i]+32);
        else
            printf("%c", str[i]);
    }

    printf("\nSentence Case: ");
    int started = 0;
    for(i=0; str[i]!='\0'; i++)
    {
        if(started==0)
        {
            if(!started && str[i]>='a' && str[i]<='z')
            {
                printf("%c", str[i]-32);
                started = 1;
            }
            else if(!started && str[i]>='A' && str[i]<='Z')
            {
                printf("%c", str[i]);
                started = 1;
            }
            else if(!started && str[i]>='A' && str[i]<='Z')
               {
				printf("%c", str[i]+32);
            }
			else
               {
			    printf("%c", str[i]);
			}
        }
           
        
    }

    return 0;
}

