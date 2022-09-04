#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef uint8_t BYTE;

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

    BYTE buffer[512];
    int count = -1;
    char filename[8];
    FILE *recovered_img;

    while(fread(buffer, 512, 1, file))
    {
        if(buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            //if it is not the first image
            if (count > -1)
            {
                fclose(recovered_img);
            }
            //else it can start reading the images
            count++;
            sprintf(filename,  "%03i.jpg", count);
            recovered_img = fopen(filename, "w");
            if (recovered_img == NULL)
            {
                fclose(file);
                printf("Couldn't create recovery image file.\n");
                return 1;
            }
        }
        if (count > -1)
        {
            fwrite(buffer, 512, 1, recovered_img);
        }
    }

        fclose(file);

        if (!recovered_img)
        {
            printf("Can't recover the files try a different file.");
        }
        else
        {
            fclose(recovered_img);
        }
        return 0;
}



