#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    int votes;
    string name;
} candidate;

candidate candidates[9];

int candidate_count;

bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }
    candidate_count = argc - 1;
    if (candidate_count > 9)
    {
        printf("Maximum number of candidates is 9\n");
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int nr_vot = get_int("Number of voters: ");

    for (int i = 0; i < nr_vot; i++)
    {
        string name = get_string("Vote: ");
        if (!vote(name))
            printf("Invalid vote\n");
    }
    print_winner();
    return 0;
}

bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

void print_winner(void)
{
    int maxi = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > maxi)
            maxi = candidates[i].votes;
    }
    for (int i = 0; i < candidate_count; i++)
        if (candidates[i].votes == maxi)
            printf("%s\n", candidates[i].name);
}
