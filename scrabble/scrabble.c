#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char alphabets[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int compute_score(string word);
int return_pos(char al); //function take in the alphabet and return the position in array

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

/**-------Function Implementation-------------**/
int compute_score(string word)
{
    // TODO: Compute and return score for string
    int i = 0, total_score = 0, character_pos;
    while (word[i] != '\0')
    {
        if (isalpha(word[i]))
        {
            character_pos = return_pos(word[i]);
            total_score += POINTS[character_pos];
        }
        else
        {
            total_score += 0;
        }
        i++;
    }
    return total_score;
}

int return_pos(char ch)
{
    int i = 0;
    while (toupper(ch) != alphabets[i])
    {
        i++;
    }
    return i;
}