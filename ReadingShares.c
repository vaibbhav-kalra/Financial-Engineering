//opening a file for reading contents of a file line by line
#include<stdio.h>
int main(void)
{
	unsigned int AadharId;
	char nameOfShares[30];
	unsigned int NoOfShares;
	FILE *cfptr;
	if((cfptr=fopen("Shares.txt","r"))== NULL)//for read mode, a file should already exist
	puts("File could not be opened");
	else
	{
		printf("%-10s %-13s %s\n","AadharId","nameOfShares","NoOfShares");
		fscanf(cfptr,"%d %29s %d",&AadharId,&nameOfShares,&NoOfShares);
		while(!feof(cfptr))
		{           /*if file is there but its empty. It would have only EOF value and pointer feof will give a non 
					zero value and negation of that would be zero and so loop will not run*/
			printf("%-10d %-13s %7.2d\n",AadharId,nameOfShares,NoOfShares);
			fscanf(cfptr,"%d %29s %d",&AadharId, &nameOfShares, &NoOfShares);
		}
		fclose(cfptr);
	}
return 0;
}

