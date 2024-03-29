#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
long convert(string input);
int number = 0;
int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%li\n", convert(input));
}

long convert(string input)
{
    // TODO
    int n = strlen(input);

    if (n == 0)
    {
        return number;
    }
    char last_digit = input[n - 1];
    long converted_last_digit = last_digit - '0';
    input[n-1] = '\0';

    return converted_last_digit + 10 * convert(input);
}