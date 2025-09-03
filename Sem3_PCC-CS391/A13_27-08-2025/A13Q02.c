// Palindrome Linked List

#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data;
    struct Node* next;
};

struct Node* createNode(char data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertEnd(struct Node** head, char data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

int isPalindrome(struct Node* head) {
    int len = 0;
    struct Node* temp = head;
    while (temp) {
        len++;
        temp = temp->next;
    }

    char *arr = (char*)malloc(len * sizeof(char));
    temp = head;
    for (int i = 0; i < len; i++) {
        arr[i] = temp->data;
        temp = temp->next;
    }

    for (int i = 0; i < len/2; i++) {
        if (arr[i] != arr[len - i - 1]) {
            free(arr);
            return 0;
        }
    }
    free(arr);
    return 1;
}

int main() {
    struct Node* head = NULL;
    insertEnd(&head, 'R');
    insertEnd(&head, 'A');
    insertEnd(&head, 'D');
    insertEnd(&head, 'A');
    insertEnd(&head, 'R');

    if (isPalindrome(head))
        printf("The linked list is a Palindrome\n");
    else
        printf("The linked list is NOT a Palindrome\n");

    return 0;
}
