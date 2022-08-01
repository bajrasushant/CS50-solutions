#include<stdio.h>
#include<math.h>
#include<cs50.h>

int luhn(long int c_num)
{
    int temp_last = 0, temp_second_last = 0;
    int sum_last = 0, sum_second_last = 0;

    while(c_num!=0)
    {
        temp_last = c_num % 10;
        c_num =c_num / 10;
        temp_second_last = c_num % 10;
        c_num = c_num / 10;
        sum_last = sum_last + temp_last;
        int temp_temp_second_last;
        temp_temp_second_last = 2*temp_second_last;
        if(temp_temp_second_last > 10)
        {
            int temp_rem_last;
            temp_rem_last = temp_temp_second_last % 10;
            temp_temp_second_last = temp_temp_second_last /10;
            sum_second_last = sum_second_last + temp_rem_last + temp_temp_second_last;

        }
        else
        {
            sum_second_last = sum_second_last + temp_temp_second_last;
        }
    }
    // printf("Sum last is: %d\n", sum_last);
    // printf("Sum second last is: %d\n", sum_second_last);
    return (sum_last+sum_second_last);
}


void card_company(int card)
{
    int card_length = log10(card) + 1; //finds card length
    int start_two; //for finding the first two digits
    start_two = card/(pow(10, card_length - 2));
    int start_one;
    start_one = card/pow(10, card_length - 1);
    if(start_two == 34 || start_two == 37)
    {
        printf("AMEX\n");
    }
    else if (start_two == 51 || start_two == 52 || start_two == 53 || start_two == 54 || start_two == 55)
    {
        printf("MASTERCARD\n");
    }
    else if(start_one == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("A valid card. But don't know the origin.\n");
    }
}


int main(void)
{
    long int card_number = get_long("Number: ");
    int sum;
    sum = luhn(card_number);
    if(sum % 10 == 0)
    {
        //printf("Valid");
        card_company(card_number);
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}