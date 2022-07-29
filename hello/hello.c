#include<stdio.h>
#include<cs50.h>

int main(void)
{
    string so_and_so = get_string("What is your name: ");

    printf("Hello, %s\n", so_and_so);
}