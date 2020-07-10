#include<stdio.h>
void main()
{
    int i,j,n,b=0,c[20];
    printf("Enter the value for n");
    scanf("%d",&n);
    int h[10]={};
    int a[n];
    printf("Enter the array value");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        h[(a[i]/10)-1]=h[(a[i]/10)-1]+1;
        
    }
    
    for(i=0;i<n;i++)
    {
    h[i]=h[i]/2;
    b=b+h[i];
    }
    printf("%d",b);
}