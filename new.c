#include <stdio.h>
#include <cs50.h>

int j = 205;
int globalvar(int c);
int main(void)
{
    int i = 10;
    int prodsum = 0;


    for (i = 0; i < 5; i++)
    {
        int j = 0;
        for (j = 0; j < 2; j++)
        {
            printf("%i\n",i);
            printf("%i\n",j);
            prodsum = prodsum + i * j;
        }
    }

    printf("Ouside the for loop\n");
    printf("%i\n",i);
    printf("%i\n",j);
    printf("%i\n",prodsum);
    globalvar(j);
}
int globalvar(int c)
{
    printf("j in main%i\n",c);
    printf("j outside main %i\n",j);
}