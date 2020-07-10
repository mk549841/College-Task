#include<stdio.h>
main()
{
    int array[10]={1,2,3,4,5,6,7,8,9};
    int i;
    for(i=0;i<10;i++)
    {
        printf("\nArray value is %d in address%u\n",array[i],&array[i]);
    }
    }