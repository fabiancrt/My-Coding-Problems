#include <cs50.h>
#include <stdio.h>

int main()
{   int cntr=0;
    int change;
    do{
    change = get_int("Change owed: ");
    }while(change<0);
    while (change>=25)
    {   cntr++;
        change -= 25;
    }
    while(change>=10)
    {   cntr++;
        change -= 10;
    }
    while(change>=5)
    {   cntr++;
        change -= 5;
    }
    while(change>0)
    {   cntr++;
        change -= 1;
    }
printf("%d",cntr);
printf("\n");
}

