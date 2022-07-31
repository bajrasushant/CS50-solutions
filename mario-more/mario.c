#include<stdio.h>
#include<cs50.h>
void pyramid(int h)
{
    for(int i = 1; i <= h; i++)
    {
        for(int j = h; j > 0; j--)
        {
            if(i>=j)
            {
                printf("#");
            }
            else
            {
            printf(" ");
            }
        }
        printf("  ");
        for(int j = 1; j <= h; j++)
        {
            if(i>=j)
            {
                printf("#");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }while((height <= 0) || (height > 8));
    pyramid(height);
    return 0;
}