#include "helpers.h"
#include <math.h>

int checkColour(int a);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int grey_color;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // if (image[i][j].rgbtBlue > image[i][j].rgbtGreen && image[i][j].rgbtBlue > image[i][j].rgbtRed)
            // {
            //     grey_colour = image[i][j].rgbtBlue;
            // }
            // else if (image[i][j].rgbtBlue < image[i][j].rgbtGreen && image[i][j].rgbtGreen > image[i][j].rgbtRed)
            // {
            //     grey_colour = image[i][j].rgbtGreen;
            // }
            // else
            // {
            //     grey_colour = image[i][j].rgbtRed;
            // }
            int grey_shade;
            grey_shade = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = grey_shade;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed, originalGreen, originalBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalBlue = image[i][j].rgbtBlue;
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;

            int sepiaRed = checkColour(round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue));
            int sepiaGreen = checkColour(round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue));
            int sepiaBlue = checkColour(round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue));


            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

int checkColour(int a)
{
    if (a > 255)
    {
        return 255;
    }
    else if (a < 0)
    {
        return 0;
    }
    else
    {
        return a;
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int tempRed, tempGreen, tempBlue;
        for (int j = 0, k = width - 1; j <= floor(width / 2); j++)
        {
            tempRed = image[i][j].rgbtRed;
            tempGreen = image[i][j].rgbtGreen;
            tempBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][k].rgbtRed;
            image[i][j].rgbtGreen = image[i][k].rgbtGreen;
            image[i][j].rgbtBlue =  image[i][k].rgbtBlue;

            image[i][k].rgbtRed = tempRed;
            image[i][k].rgbtGreen = tempGreen;
            image[i][k].rgbtBlue = tempBlue;

            k--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;

            double sumNeighRed = 0, sumNeighBlue = 0, sumNeighGreen = 0;

            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if ( k >= 0 && l >= 0 && k < height && l < width)
                    {
                        sumNeighBlue += image[k][l].rgbtBlue;
                        sumNeighGreen += image[k][l].rgbtGreen;
                        sumNeighRed += image[k][l].rgbtRed;

                        count++;
                    }
                }
            }
            image[i][j].rgbtBlue = round(sumNeighBlue / count);
            image[i][j].rgbtGreen = round(sumNeighGreen / count);
            image[i][j].rgbtRed = round(sumNeighRed / count);
        }
    }
    return;
}
