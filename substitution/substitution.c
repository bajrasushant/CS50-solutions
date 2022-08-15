#include <cs50.h>
#include <stdio.h>
#include<ctype.h>
#include<string.h>

// string substitution(string s, string key);
int finding_chars(char find_s)
{
    string abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i = 0;
    while (abcd[i] != toupper(find_s))
    {
        i++;
    }
    return i;
}

int main(int argc, string argv[])
{
    string key = argv[1];
    if (argc == 2)
    {
        int count = 0;
        for (int i = 0; i < 26; i++)
        {
            if (!isalpha(key[i]))
            {
                printf("Values in key should be alphabets only.\n");
                return 1;
            }
        }
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            for (int j = i + 1; j <= strlen(argv[1]); j++)
            {
                if (key[i] == key[j])
                {
                    count++;
                }
            }
        }

        if (strlen(argv[1]) != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        else if (count >= 1)
        {
            printf("Duplicate values in key.\n");
            return 1;
        }
        else
        {
            string s;
            char new_text[512] = {0};
            s = get_string("plaintext: ");
            //cipher_text = substitution(plain_text, argv[1]);
           // printf("%s", key);
            for (int i = 0; i <= strlen(s); i++)
            {
                if(isalpha(s[i]))
                {
                    int location = finding_chars(s[i]);
               //     printf("%d\n", location);
                    if (isupper(s[i]))
                    {
                        new_text[i] = toupper(key[location]);
                    }
                    else
                    {
                        new_text[i] = tolower(key[location]);
                    }
                }
                else
                {
                    new_text[i] = s[i];
                }
            }
            printf("ciphertext: %s", new_text);
            printf("\n");
            return 0;
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

}

/**----------Function Definition-----------**/

// string substitution(string s, string key)
// {
//     string new_text = NULL;
//     for (int i = 0; i <= strlen(s); i++)
//     {
//         if(isalpha(s[i]))
//         {
//             if(isupper(s[i]))
//             {
//                 new_text[i] = toupper(key[i]);
//             }
//             else
//             {
//                 new_text[i] = tolower(key[i]);
//             }
//         }
//         else
//         {
//             new_text[i] = s[i];
//         }
//     }
//     return new_text;
// }
