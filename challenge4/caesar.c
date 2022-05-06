#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char text[1000000];
    printf("Enter the text: ");
    scanf("%s", text);
    printf("\n");
    int shift;
    printf("Enter the shift: ");
    scanf("%i", &shift);

    char alphabet[] = "abcdefghijklmnopqrstuvwxyz";

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            int index = 0;
            for (int x = 0; x < strlen(alphabet); x++)
            {
                if (alphabet[x] == text[i])
                {
                    break;
                }
                index++;
            }
            int aindex = (index + shift) % 26;
            printf("%c", alphabet[aindex]);
        }
        else
        {
            printf("%c", text[i]);
        }
    }
    printf("\n");
}