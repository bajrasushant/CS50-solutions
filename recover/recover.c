#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover [filename]");
        return 1;
    }

    FILE *file;
    if (
        file = fopen(argv[1], "r");

}