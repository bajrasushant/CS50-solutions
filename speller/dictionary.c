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

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
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
    do
    {
        fscanf(dictionary_file, "%s", words);
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            printf("Failed. Try again. \n");
        }
        strcpy(new_node->word, words);

        int hash_num = hash(new_node->word);

        if (table[hash_num]->next != NULL)
        {
            new_node->next = table[hash_num]->next;
        }

        table[hash_num]->next = new_node;

        free(new_node);

    } while(words != EOF);
    fclose(dictionary_file);

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
