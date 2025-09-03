// Find Frequency of a Value in DLL

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

int frequency(struct Node* head, int val) {
    int count = 0;
    struct Node* temp = head;
    while (temp != NULL) {
        if (temp->data == val)
            count++;
        temp = temp->next;
    }
    return count;
}

int main() {
    struct Node* dll = NULL;

    insertEnd(&dll, 1);
    insertEnd(&dll, 2);
    insertEnd(&dll, 3);
    insertEnd(&dll, 2);
    insertEnd(&dll, 4);
    insertEnd(&dll, 2);

    int val = 2;
    printf("Frequency of %d = %d\n", val, frequency(dll, val));

    return 0;
}
