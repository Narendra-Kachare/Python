/////////////////////////////////////////////////
// Header
/////////////////////////////////////////////////

#include<stdio.h>
#include<stdlib.h>

/////////////////////////////////////////////////
// Helper function
/////////////////////////////////////////////////

int iMax(int *ptr,int Length)
{
    int Max = ptr[0];
    for (int i = 1; i < Length; i++)
    {
        if(Max < ptr[i])
        {
            Max = ptr[i];
        }
    }
    return Max;
}


/////////////////////////////////////////////////
// Entry point function
/////////////////////////////////////////////////
int main()
{
    int iLength = 0;
    int iRet = 0;
    int *Arr = NULL;

    printf("Enter number of elements : \n");
    scanf("%d",&iLength);

    Arr = (int*)malloc(sizeof(int)*iLength);
    printf("Enter the elements : \n");
    for (int i = 0; i < iLength; i++)
    {
        scanf("%d",&Arr[i]);
    }
    printf("Enter elements are : \n");
    for (int i = 0; i < iLength; i++)
    {
        printf("%d\t",Arr[i]);
    }
    printf("\n");
    iRet = iMax(Arr,iLength);
    printf("Maximum element of the array is : %d\n",iRet);
    


    return 0;
}
