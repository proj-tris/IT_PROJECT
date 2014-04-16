#include <stdio.h>

extern void prefix_sum(int *data, int size);

int main()
{
	int size, i;
	scanf("%d", &size);
	int data[size];
	for (i = 0; i < size; i++)
	{
		scanf("%d", &data[i]);
	}
	prefix_sum(data, size);
	for (i = 0; i < size; i++)
	{
		printf("%d ", data[i]);
	}
	printf("\n");
	return 0;	
}