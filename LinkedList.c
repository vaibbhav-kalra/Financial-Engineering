#include<stdio.h>
 struct ListNode{
 	int data;
 	struct ListNode *next;//pointer to next node(structure)
 };
 typedef struct ListNode List;//typedef is for creating synonyms
 typedef List * ListPtr;
 void insert(ListPtr *ptr, int value);
 int delete(ListPtr *ptr, int value);
 
 void insert(ListPtr *ptr, int value)
 {
 	ListPtr newPtr;//ListPtr prevPtr;
 	newPtr = (ListPtr) malloc(sizeof(struct ListNode));//creating element of type ListNode and size same as of ListNode
 	if(newPtr != NULL){
 		newPtr -> data=value;//for accessing pointers use arrow operator
 		newPtr -> next=*ptr;//address of next node being stored in the new node to be inserted
 		*ptr=newPtr;
 		printf("insert %d\n",value);
	 }
	 else{
	 	printf("Insufficeient memory");
	 }
 }
 int delete(ListPtr *ptr, int value)
 {
 	ListPtr tempPtr;
 	ListPtr prevPtr, currentPtr;
 	if(value== (*ptr) -> data){
 		tempPtr = *ptr;
 		*ptr =(*ptr) -> next;
 		free (tempPtr);
 		printf("delete %d\n",value);
 		return value;
	 }
	 else{
	 	prevPtr = *ptr;
	 	currentPtr= (*ptr) -> next;
	 	while (currentPtr -> data!=value && currentPtr != NULL)
	 	{
	 		tempPtr = currentPtr;
	 		currentPtr = currentPtr -> next;
	 		prevPtr = tempPtr;
		 }
		 if(currentPtr -> data == value)
		 {
		 	tempPtr = currentPtr;
		 	prevPtr -> next = currentPtr -> next;
		 	free (tempPtr);
		 	printf("delete %d\n",value);
		 	return value;
		 }
		 else{return -1;
		 }
	 }
 }
 int main(void)
 {
 	ListPtr node;
 	insert (&node, 10);
 	insert (&node, 20);
 	insert (&node, 20);
 	delete (&node,10);
	getch();
	return 0;
 }
