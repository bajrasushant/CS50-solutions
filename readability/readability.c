#include<stdio.h>
#include<math.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
    string text = get_string("Text: ");
    int letters, words, sentences;
    letters = count_letters(text);
    //printf("letters: %d\n", letters);
    words = count_words(text);
    //printf("words: %d\n", words);
    sentences = count_sentences(text);
    //printf("sentences: %d\n", sentences);
    float l = (letters / (float) words) * 100;
    // printf("%f\n", l);
    float s = (sentences / (float) words) * 100;
    //printf("%f\n", s);
    int index;
    float no_round_index = (0.0588 * l) - (0.296 * s) - 15.8;
    // printf("%f\n",no_round_index);
    index = (int)round(no_round_index);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}
/**---------function Implementation-----------**/
//letter counting
int count_letters(string s)
{
    int nums_letter = 0;
    for (int i = 0; i < strlen(s) ; i++)
    {
        if (!isalnum(s[i]))
        {
            continue;
        }
        else
        {
            nums_letter++;
        }
    }
    return nums_letter;
}
//word counting
int count_words(string s)
{
    int nums_words = 0;
    for (int i = 0; i < strlen(s) ; i++)
    {
        if (s[i] == ' ')
        {
            nums_words++;
        }
        else
        {
            continue;
        }
    }
    nums_words++;
    return nums_words;

}
//sentence counting
int count_sentences(string s)
{
    int nums_sentences = 0;
    for (int i = 0; i < strlen(s) ; i++)
    {
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')
        {
            nums_sentences++;
        }
        else
        {
            continue;
        }
    }
    return nums_sentences;
}
//all the functions can be implemented within a single function as well