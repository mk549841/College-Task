#include<stdio.h>
void main()
{
    int i, j,pri,sweet,chair,p=0;
    scanf("%d%d%d",&pri,&sweet,&chair);
    for(i=chair;i<(sweet+chair);i++)
    {
        if(p==pri)
        {
            p=0;
        }
        p++;
    }
    printf("%d",p);
}
