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
    else
    {

    }
}

int ask_for_height(void)
{
    int height;
    height = get_int("Height:");
}

int main(void)
{
    int h = ask_for_height();
    pyramid(h);
}