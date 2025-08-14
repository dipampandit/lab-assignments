// Circular Queue using Pointers

#include <stdio.h>
#include <stdlib.h>

#define SIZE 5

int *queue;
int front = -1, rear = -1;

int isFull() {
    return ((rear + 1) % SIZE == front);
}

int isEmpty() {
    return (front == -1);
}

void enqueue(int value) {
    if (isFull()) {
        printf("Queue is FULL!\n");
        return;
    }
    if (isEmpty())
        front = 0;
    rear = (rear + 1) % SIZE;
    *(queue + rear) = value;
    printf("%d inserted.\n", value);
}

void dequeue() {
    if (isEmpty()) {
        printf("Queue is EMPTY!\n");
        return;
    }
    printf("%d deleted.\n", *(queue + front));
    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % SIZE;
    }
}

void display() {
    if (isEmpty()) {
        printf("Queue is EMPTY!\n");
        return;
    }
    printf("Queue: ");
    int i = front;
    while (1) {
        printf("%d ", *(queue + i));
        if (i == rear)
            break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    queue = (int *)malloc(SIZE * sizeof(int));

    int choice, value;

    while (1) {
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                enqueue(value);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                free(queue);
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }
}
