#include<stdio.h>
#include<string.h>
int main()
{
    char name[100];
    int i,j;
    gets(name);
    for(i=0;name[i]!=NULL;i++)
    {
        while (!(name[i]>='a' && name[i]<='z')||(name[i]>='A' && name[i]<='Z'||name[i]==NULL))
        {
            for(j=i;name[j]!=NULL;j++)
            {
                name[j]=name[j+1];
            }
            name[j]=NULL;
        }
    }
    puts(name);
    return 0;
}