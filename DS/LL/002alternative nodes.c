#include <stdio.h> 
#include <stdlib.h>
struct Node { 
    int data; 
    struct Node* next; 
}*head=NULL; 
void printAlternateNode() 
{ 
    int count = 0; 
  
    while (head != NULL) { 
  
        // when count is even print the nodes 
        if (count % 2 == 0)  
            printf(" %d ", head->data); 
  
        // count the nodes 
        count++; 
  
        // move on the next node. 
        head = head->next; 
    } 
} 
  
void push(int new_data) 
{ 
    struct Node* new_node =(struct Node*)malloc(sizeof(struct Node)); 
    new_node->data = new_data; 
    new_node->next =head; 
    head= new_node; 
} 
void main() 
{
    struct Node* head = NULL;
    push(12); 
    push(29); 
    push(11); 
    push(23); 
    push(8); 
    printAlternateNode(); 
} 
