#include <stdio.h>
#include <cs50.h>
int main(void)
{
    //Prints ascii value of given string
    int i,n;
    n = get_int("How many numbers are there\n");
    int num[n];
    printf("Enter a NUMBERS separated with space\n");
    for(i=0; i<n; i++)
    {
        scanf("%d",&num[i]);
    }
    for(i=0; i<n; i++)
    {
        printf("%c",num[i]);
    }
    printf("\n");
}