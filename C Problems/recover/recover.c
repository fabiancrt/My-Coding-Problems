#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    //char *input_file_name = argv[1];
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("Error: cannot open %s\n", argv[1]);
        return 2;
    }
    int cntr = 0;
    BYTE buffer[512];
    FILE *img_p = NULL;
    char fname[8];

    while (fread(&buffer, 512, 1, f) == 1)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (!(cntr == 0))
            {
                fclose(img_p);
            }
            sprintf(fname, "%03i.jpg", cntr);
            img_p = fopen(fname, "w");
            cntr++;
        }
        if (!(cntr == 0))
        {
            fwrite(&buffer, 512, 1, img_p);
        }
    }
        fclose(f);
        fclose(img_p);
        return 0;
}
