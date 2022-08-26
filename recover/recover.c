#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover [filename]\n");
        return 1;
    }

    FILE *file;
    file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("File cannot be opened\n");
        return 1;
    }
    //fread(data,size,number,inptr) data-> to store data you're reading
    //size->size of each element to read number->number of elements to read inptr->File to read from

    char buffer[512];
    int count;
    char filename[3];
    FILE *recovered_img;

    while(fread(buffer, 512, 1, file))
    {
        if(buffer[0] = 0xff &&
            buffer[1] = 0xd8 &&
            buffer[2] = 0xff &&
            (buffer[3] & 0xf0) == 0ex0)
        {
            sprintf(filename,  "%03i.jpg", count);
            recovered_img = fopen(filename, "w");
            count++;
            


}