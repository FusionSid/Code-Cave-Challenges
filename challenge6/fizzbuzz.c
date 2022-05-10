#include <stdio.h>

void fizzbuzz(int num);

int main()
{
    for (int i = 0; i <= 100; i++)
    {
        fizzbuzz(i);
        printf("\n");
    }
    return 0;
}

void fizzbuzz(int num)
{
    if (num % 3 == 0 && num % 5 == 0)
    {
        printf("Fizz Buzz");
    } 
    else if (num % 3 == 0)
    {
        printf("Fizz");
    }
    else if (num % 5 == 0)
    {
        printf("Buzz");
    }
    else 
    {
        printf("%i", num);
    }
}