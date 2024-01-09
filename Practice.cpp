#include<iostream>
using namespace std;

int main()
{   
    int iValue = 0;
    int *ptr = NULL;

    cout<<"Enter the number of elements : \n";
    cin>>iValue;

    cout<<"Enter the elements : \n";
    ptr = new int(iValue);

    for (int i = 0; i < iValue; i++)
    {
        cin>>ptr[i];
    }
    cout<<"Enter elements  are: \n";

    for (int i = 0; i < iValue; i++)
    {
        cout<<ptr[i]<<"\t";
    }

    free(ptr);
    for (int i = 0; i < iValue; i++)
    {
        cout<<ptr[i]<<"\t";
    }



    return 0;
}