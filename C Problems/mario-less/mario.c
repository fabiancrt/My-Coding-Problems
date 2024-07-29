#include <cs50.h>
#include <stdio.h>

int main()
{   int height;
    int i;
    int j;
   do{
    height = get_int("Height: ");
   }while(height<1 || height>8);

   for(i=1;i<=height;i++){
   for(j=1;j<=height;j++)
   if(i+j>height+1 || i+j==height+1)
        printf("#");
        else
        printf(" ");
        printf("\n");
   }

return 0;
}
