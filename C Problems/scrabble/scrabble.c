#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main ()
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");
    int s1=0,s2=0;
    //TOPUPPER
 for (int i = 0; player1[i]!='\0'; i++) {
      if(player1[i] >= 'a' && player1[i] <= 'z')
         player1[i] = player1[i] -32;
      }
       for (int i = 0; player2[i]!='\0'; i++) {
      if(player2[i] >= 'a' && player2[i] <= 'z')
         player2[i] = player2[i] -32;
      }
      //SUM1
    for (int i = 0; player1[i]!='\0'; i++) {
      if(strchr("AEILORSTU",player1[i]))
       s1+=1;
       else if(strchr("DG",player1[i]))
       s1+=2;
       else if(strchr("BCMP",player1[i]))
       s1+=3;
       else if(strchr("FHVWY",player1[i]))
       s1+=4;
       else if(strchr("K",player1[i]))
       s1+=5;
       else if(strchr("JX",player1[i]))
       s1+=8;
       else if(strchr("QZ",player1[i]))
       s1+=10;
       else
         s1+= 0;
      }
      //SUM2
          for (int i = 0; player2[i]!='\0'; i++) {
      if(strchr("AEILORSTU",player2[i]))
       s2+=1;
       else if(strchr("DG",player2[i]))
       s2+=2;
       else if(strchr("BCMP",player2[i]))
       s2+=3;
       else if(strchr("FHVWY",player2[i]))
       s2+=4;
       else if(strchr("K",player2[i]))
       s2+=5;
       else if(strchr("JX",player2[i]))
       s2+=8;
       else if(strchr("QZ",player2[i]))
       s2+=10;
       else
         s2+= 0;
      }

    if(s1==s2)
    printf("Tie!\n");
    if(s1>s2)
    printf("Player 1 wins!\n");
    if(s1<s2)
    printf("Player 2 wins!\n");
}
