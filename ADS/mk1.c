#include<stdio.h>
#include<math.h>
#include<string.h>
main()
{
	int arr[100];
	char b[100];
	gets(b);
	int len=strlen(b);
	int n=len;
	int a=atoi(b);
	int k,i,j,s,q,p,l,sum=0;
	for(k=len-1;k>=0;k--)
	{
		arr[k]=a%10;
		a=a/10;
	}
	for(j=0;j<n;j++)
	{
		for(i=j;i<n;i++)
		{
			s=0;
			k=0;
			l=i;
			while((k<=i)&&(k<=j))
			{
				p=1;
				for(q=1;q<=k;q++)
					p=p*10;
				s=s+arr[l--]*p;
				k++;
			}
			sum=sum+s;
		}
	}
	printf("%d",sum);
}
