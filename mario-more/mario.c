#include <cs50.h>
#include <stdio.h>

void pyramid(int h)
{
    if(h>0 && h<=8)
    {
        for(int i = h; i < 0; i--)
        {
            printf("#\n");
        }
    }
}

int main(void)
{
    int height = get_int("Height: ");
    pyramid(height);
}