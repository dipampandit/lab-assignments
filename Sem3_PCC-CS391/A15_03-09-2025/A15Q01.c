// Check if DLL is Palindrome

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = newNode->next = NULL;
    return newNode;
}

void insertEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
}

int isPalindrome(struct Node* head) {
    if (head == NULL || head->next == NULL)
        return 1;
    struct Node* left = head;
    struct Node* right = head;
    while (right->next != NULL)
        right = right->next;
    while (left != right && right->next != left) {
        if (left->data != right->data)
            return 0;
        left = left->next;
        right = right->prev;
    }
    return 1;
}

int main() {
    struct Node* dll = NULL;

    insertEnd(&dll, 1);
    insertEnd(&dll, 2);
    insertEnd(&dll, 3);
    insertEnd(&dll, 2);
    insertEnd(&dll, 1);

    if (isPalindrome(dll))
        printf("DLL is a Palindrome\n");
    else
        printf("DLL is NOT a Palindrome\n");

    return 0;
}
