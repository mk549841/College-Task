#include<stdio.h>
int main()
{
	int n,k;
	printf("Entr the n\n");
	scanf("%d",&n);
	printf("The the time taken in seconds\n");
	scanf("%d",&k);
	printf("Enter the element one by one\n");
	int a[n],b[n],i,sum=0;
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Enter the element one by one\n");
	for(i=0;i<n;i++)
		scanf("%d",&b[i]);
	int max=b[0];
	for(i=0;i<n;i++)
	{
		if(b[i]>max)
			max=b[i];
	}
	int m=max+1;
	for(i=0;i<n;i++)
	{
		if(m-a[i]>=0)
		{
		sum=sum+( (m-a[i]) *k);
		}
	}
printf("%d",sum);
return 0;
}

