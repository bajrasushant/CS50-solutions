// Implements a dictionary's functionality

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

char *words;

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
    if (strcasecmp(ptr->word, word) == 0)
    {
        return true;
    }
    else
    {
        while(ptr != NULL)
        {
            if ((strcasecmp(ptr->word, word)) == 0)
            {
                return true;
            }
            ptr = ptr->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int i = 0;

    for (int j = 0; j < LENGTH; j++)
    {
        i += tolower((unsigned int)word[j]);
    }
    return i;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dictionary_file;
    dictionary_file = fopen("dictionary", "r");
    if (dictionary_file == NULL)
    {
        printf("Couldn't open file. Try again.\n");
        return false;
    }
    while(fgets(words, LENGTH, dictionary_file))
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Failed. Try again. \n");
            return false;
        }
        strcpy(new_node->word, words);

        int hash_num = hash(words);

        if (table[hash_num]->next != NULL)
        {
            new_node->next = table[hash_num]->next;
        }

        table[hash_num]->next = new_node;

        words_dict++;

    }

    fclose(dictionary_file);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if(words_dict == 0)
    {
        return 0;
    }
    return words_dict;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
