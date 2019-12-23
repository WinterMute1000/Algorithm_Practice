#include <stdio.h>
#include <stdbool.h>

int main(void)
{
	int num=0,palin_left=1,palin_right=1;
	_Bool is_palin=true;

	printf("Input:");
	scanf("%d",&num);

	if(num<0)
	{
		printf("false\n");
		return 0;
	}

	while(palin_left*10<=num)
		palin_left*=10;

	while(palin_left>palin_right)
	{
		if((num/palin_left)%10!=(num/palin_right)%10)
		{	
			is_palin=false;
			break;
		}

		palin_left/=10;
		palin_right*=10;
	}

	if(is_palin)
		printf("true\n");
	else
		printf("false\n");
}


