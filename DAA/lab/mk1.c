#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main(){
    int i, j, k, n, h;
    int ar[100000];
    int area, max=0;
    scanf("%d",&n);
    for(i=0;i<=n;++i)
        scanf("%d",&ar[i]);
    for(i=0;i<=n;++i)
        {
        int c = 1;
        j = i-1;
        k = i+1;
        while(j>=0 && ar[j]>ar[i]){
            j--;
            c++;}
        while(k<=n && ar[k]>ar[i]){
            k++;
            c++;}
        area = c * ar[i];
        max = (area>max)? area : max;}
    
    printf("%d",max);
    return 0;}
