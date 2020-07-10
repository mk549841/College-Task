#include<stdio.h>
void main()
{
	int i ,j,temp;
	int pris,chair,sweets;
	printf("Enter how MAny in prisonars");
	scanf("%d",&pris)
	temp=chair;
	for(i=0;i<sweets;i++)
	{
		if(temp==pris)
			temp=0;
		temp++;
	}
	printf("%d\n",--temp);
	
}
			
