#include <stdio.h>
int in=0,max=0;
void minheapinsert(int a[],int marks)
{
	in++;
	a[in]=marks;
	int i=in,temp;
	
	while(i>1)
	{
		if(a[i]<a[i/2])
		{
			temp=a[i];
			a[i]=a[i/2];
			a[i/2]=temp;
		}
		else
			break;
		i=i/2;
	}
}
void maxheapinsert(int a[],int marks)
{
	max+=1;
	a[max]=marks;
	int i=max,temp;
	
	
		while(i>1)
		{
			if(a[i]>a[i/2])
			{
				temp=a[i];
				a[i]=a[i/2];
				a[i/2]=temp;
			}
			else
				break;
			i=i/2;
		}
	
}
void deleteminheap(int heap[])
{
	int i=1,temp,ansr,k;
	heap[i]=heap[in];
	in--;
	while(1)
	{
		if ((2*i) + 1 <= max)
		{
		if(heap[i]>heap[2*i+1] || heap[i]>heap[2*i] )
		{
			if(heap[2*i+1] < heap[2*i])
				k=2*i+1;
			else
				k=2*i;
		
			temp=heap[k];
			heap[k]=heap[i];
			heap[i]=temp;
			i=k;
		}
		else
			break;
		}
		else 
		{
			if (2*i<=max)
			{
				if(heap[i]>heap[2*i])
				{
					int tmp;
					tmp=heap[i];
					heap[i]=heap[2*i];
					heap[2*i]=tmp;
					i=2*i;	
				}
				else
					break;
			}
		}
		if (2*i>max && (2*i)+1>max)
			break;
	}
}
void deletemaxheap(int heap[])
{
	int ansr,temp,i=1,k;
	heap[i]=heap[max];
	max-=1;
	while(1)
	{
		if ((2*i) + 1 <= max)
		{
		if(heap[i]<heap[2*i+1] || heap[i]<heap[2*i] )
		{
			if(heap[2*i+1] > heap[2*i])
				k=2*i+1;
			else
				k=2*i;
			temp=heap[k];
			heap[k]=heap[i];
			heap[i]=temp;
			i=k;
		}
		else
			break;
		}
		else 
		{
			if (2*i<=max)
			{
				if(heap[i]<heap[2*i])
				{
					int tmp;
					tmp=heap[i];
					heap[i]=heap[2*i];
					heap[2*i]=tmp;
					i=2*i;	
				}
				else
					break;
			}
		}
		if (2*i>max && (2*i)+1>max)
			break;
	}
}
int main()
{
	int j,t,i,ind,marks,a[100000],heap[100000],cnt=0,temp;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&ind);
		if(ind==1)
		{
			if(in==0)
				printf("%d\n",-1);
			else
			{
				printf("%d\n",a[1]);
			}
		}
		else
		{
			scanf("%d",&marks);
			cnt++;
			if(in>0)
			{
				if(marks>a[1])
				{
					temp=a[1];
					deleteminheap(a);
					minheapinsert(a,marks);
					maxheapinsert(heap,temp);
				}
				else
					maxheapinsert(heap,marks);
			}
			else
				maxheapinsert(heap,marks);
			if((max+in)%4==0)
			{
				temp=heap[1];
				deletemaxheap(heap);
				minheapinsert(a,temp);
			}
		}
	/*	printf("<--------min heap-------------->\n");
		for(j=1;j<in;j++)
			printf("%d ",a[j]);
		printf("\n<------max heap-------------->\n");
		for(j=1;j<max;j++)
			printf("%d ",heap[j]);
		printf("\n");*/

	}	
	return 0;
}
