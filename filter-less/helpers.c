#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int grey_color;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue > image[i][j].rgbtGreen && image[i][j].rgbtBlue > image[i][j].rgbtRed)
            {
                grey_colour = image[i][j].rgbtBlue;
            }
            else if (image[i][j].rgbtBlue < image[i][j].rgbtGreen && image[i][j].rgbtGreen > image[i][j].rgbtRed)
            {
                grey_colour = image[i][j].rgbtGreen;
            }
            else
            {
                grey_colour = image[i][j].rgbtRed;
            }
            int grey_shade;
            grey_shade = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3;
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = grey_shade;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
