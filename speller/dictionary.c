// Implements a dictionary's functionality

#include<stdio.h>
#include<strings.h>
#include<string.h>
#include<stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

unsigned int words_dict = 0; //tracks number of words loaded into dictionary

// TODO: Choose number of buckets in hash table
const unsigned int N = 20000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hash_nums = hash(word);
    node *ptr;
    ptr = table[hash_nums];
    while (ptr != NULL)
    {
        if ((strcasecmp(ptr->word, word)) == 0)
        {
            return true;
        }
        ptr = ptr->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int i = 0;

    for (int j = 0; j < strlen(word); j++)
    {
        i += tolower((unsigned int)word[j]);
    }
    return i % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dictionary_file;
    dictionary_file = fopen(dictionary, "r");

    if (dictionary_file == NULL)
    {
        printf("Couldn't open file. Try again.\n");
        return false;
    }

    char words[LENGTH + 1];

    while (fgets(words, LENGTH+1, dictionary_file))
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Failed. Try again. \n");
            return false;
        }

        strcpy(new_node->word, words);

        int hash_num = hash(words);

        if (table[hash_num] != NULL)
        {
            new_node->next = table[hash_num];
        }

        table[hash_num] = new_node;

        words_dict++;

    }

    fclose(dictionary_file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return words_dict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {

        node *cursor = table[i];

        if (cursor == NULL)
        {
            continue;
        }

        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }

        if (cursor == NULL && i ==N-1)
        {
            return true;
        }
    }
    return false;
}
