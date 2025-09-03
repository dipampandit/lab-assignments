// Merge Two DLLs

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

void display(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

struct Node* mergeDLL(struct Node* head1, struct Node* head2) {
    if (head1 == NULL) return head2;
    if (head2 == NULL) return head1;
    struct Node* temp = head1;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = head2;
    head2->prev = temp;
    return head1;
}

int main() {
    struct Node* dll1 = NULL;
    struct Node* dll2 = NULL;

    insertEnd(&dll1, 1);
    insertEnd(&dll1, 2);
    insertEnd(&dll1, 3);
    insertEnd(&dll1, 4);

    insertEnd(&dll2, 5);
    insertEnd(&dll2, 6);
    insertEnd(&dll2, 7);

    printf("DLL1: ");
    display(dll1);
    printf("DLL2: ");
    display(dll2);

    struct Node* merged = mergeDLL(dll1, dll2);
    printf("Merged DLL: ");
    display(merged);

    return 0;
}
