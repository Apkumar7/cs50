#include <cs50.h>
#include <stdio.h>
#include <string.h>
int encrypt();
int decrypt();
string ys;
int main(void)
{
    string e = "encrypt";
    string d = "decrypt";
    string answer;
    do
    {
        answer = get_string("Would you like to encrypt or decrypt? ");
    }
    while(strcmp(answer,e) != 0 && strcmp(answer,d) != 0);
    if (strcmp(answer,e) == 0)
    {
        printf("YOU ARE NOW ENCRYPTING!\n");
        encrypt();

    }
    else if(strcmp(answer,d) == 0)
    {
        printf("YOU ARE NOW DECRYPTING!\n");
        decrypt();

    }
}

int encrypt()
{
    string s;
    do
    {
        s = get_string("Input string to encrypt: ");
    }
    while(strlen(s) <= 0);
    for (int i = 0, n = strlen(s); i < n; i++ )
    {
        printf("%i ", s[i]);
    }
    printf("\n");
    return 0;
}

int decrypt()
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
    return 0;
}