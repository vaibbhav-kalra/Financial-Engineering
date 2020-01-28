#include<stdio.h>
int main(void)
{
	unsigned int AadharId;
	char nameOfShares[30];
	unsigned int NoOfShares;
	FILE *cfptr;//creating a file
	if((cfptr=fopen("Shares.txt","a"))== NULL)//opening file in write mode
	puts("File could not be opened");
	else{
		puts("enter the AadharId, nameOfShares and NoOfShares:");//new blank file is created if file is not already there with new inputs
		puts("\nEnter EOF to end input");//enter Ctrl+Z
		printf("%s","?");
		scanf("%d %29s %d",&AadharId, &nameOfShares, &NoOfShares);
		while(!feof(stdin)){//if fileis not empty, storing values in the file
			fprintf(cfptr,"%d %s %d\n",AadharId, nameOfShares,NoOfShares);
			printf("%s","?");
			scanf("%d %29s %d",&AadharId,&nameOfShares, &NoOfShares);
		}
		fclose(cfptr);
	}
	return 0;
}

