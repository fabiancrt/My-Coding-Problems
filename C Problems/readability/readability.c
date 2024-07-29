#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int main()
{
    int cuv = 0;
    int prop = 0;
    int lit = 0;
    string text = get_string("Text: ");
    for (int i = 0; i < strlen(text); i++)
    {
        if (strchr("?!.", text[i]))
            prop++;
    }
    char *p = strtok(text, " ,.;!?:");
    while (p)
    {
        cuv++;
        //lit += strlen(p);
        for(int i=0;i<strlen(p);i++)
        if(!strchr("'",p[i]))
        lit++;
        p = strtok(NULL, " ,.;!?:");
    }
    double calc = round((0.0588 * lit/cuv*100) - (0.296 * prop/cuv*100) - 15.8);
    //printf("%f\n",calc);
    int index = calc;
    if (index < 1)
        printf("Before Grade 1\n");
    if (index > 16)
        printf("Grade 16+\n");
    if (index > 0 && index < 17)
    {
        printf("Grade ");
        printf("%d\n", index);
    }
   //printf("%i\n",cuv);
  // printf("%i\n",prop);
   //printf("%i\n",lit);
}
