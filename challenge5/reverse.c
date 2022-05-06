#include <stdio.h>
#include <ctype.h>
#include <string.h>


char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

int main()
{
    char text[69];
    printf ("Enter text: ");  
    scanf ("%s", text);

    strrev(text);
    
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i])) 
        {
            printf("%c", tolower(text[i]));
        }
        else 
        {
            printf("%c", toupper(text[i]));
        }
    }
    printf("\n");
    return 0;  

}