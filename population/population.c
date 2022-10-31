#include <stdio.h>

int main()
{
    int start, stop, years = 0;

    do
    {
        printf("Enter the starting population size: ");
        scanf("%i", &start);
    } while (start < 9);

    do
    {
        printf("Enter the ending population size: ");
        scanf("%i", &stop);
    } while (stop < start);

    while (start < stop)
    {
        start += start / 3 - start / 4;
        years++;
    }
    printf("%i\n", years);

    return 0;
}