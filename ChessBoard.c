/*
    Create chess board using ASCII value

    Function name : Chessboard, ChessboardX
    Input         : int, int
    Output        : Chessboard Layout
    Description   : Display chessboard
    Author        : Narendra Mahadev Kachare
    Date          : 29/09/2023

*/




/////////////////////////////////////////////////
// Header
/////////////////////////////////////////////////

#include <stdio.h>
#define C1_WHITE 219
#define C2_BLACK 255


/////////////////////////////////////////////////
// Helper function
/////////////////////////////////////////////////

void Chessboard(int iLength, int iHeight)
{
    int i = 0, j = 0;
    for (j = 0; j < iHeight; j++)
    {
        for (i = 1; i <= 8; i++)
        {

            if ((i % 2 == 0))
            {
                // C1_White Colour
                for (int k = 0; k < iLength; k++)
                {
                    printf("%c", C1_WHITE);
                }
            }
            else
            {
                // C2_Black Colour
                for (int k = 0; k < iLength; k++)
                {
                    printf("%c", C2_BLACK);
                }
            }
        }
        printf("\n");
    }
}
void ChessboardX(int iLength, int iHeight)
{
    int i = 0, j = 0;
    for (j = 0; j < iHeight; j++)
    {
        for (i = 1; i <= 8; i++)
        {

            if ((i % 2 != 0))
            {
                // C1_White Colour
                for (int k = 0; k < iLength; k++)
                {
                    printf("%c", C1_WHITE);
                }
            }
            else
            {
                // C2_Black Colour
                for (int k = 0; k < iLength; k++)
                {
                    printf("%c", C2_BLACK);
                }
            }
        }
        printf("\n");
    }
}
// /////////////////////////////////////////////////
// // Entry point function
// /////////////////////////////////////////////////

int main()
{
    int iValue1 = 0, iValue2 = 0;
    printf("Enter the length of chess Box : \n");
    scanf("%d", &iValue1);
    iValue1 = 2 * iValue1;

    printf("Enter the Height of chess Box : \n");
    scanf("%d", &iValue2);

    printf("Your chess Box will be : \n\n");
    for (int j = 0; j < 8; j++)
    {
        if (j % 2 == 0)
        {
            Chessboard(iValue1, iValue2); // For Even line
        }
        else
        {
            ChessboardX(iValue1, iValue2); // For Odd Line
        }
    }

    return 0;
}
