// Priority Queue - lowest value is treated as the highest priority

#include <stdio.h>
#include <stdlib.h>

#define MAX 50

typedef struct {
    int data;
    int priority;
} Element;

Element pq[MAX];
int size = 0;

void enqueue(int value, int priority) {
    if (size == MAX) {
        printf("Priority Queue Overflow!\n");
        return;
    }
    pq[size].data = value;
    pq[size].priority = priority;
    size++;
    printf("Inserted: %d\n", value);
}

void dequeue() {
    if (size == 0) {
        printf("Priority Queue Underflow!\n");
        return;
    }

    int i, pos = 0;
    int highest = pq[0].priority;

    for (i = 1; i < size; i++) {
        if (pq[i].priority < highest) {
            highest = pq[i].priority;
            pos = i;
        }
    }

    printf("Deleted: %d\n", pq[pos].data);

    for (i = pos; i < size - 1; i++) {
        pq[i] = pq[i + 1];
    }
    size--;
}

void display() {
    if (size == 0) {
        printf("Priority Queue is empty!\n");
        return;
    }

    Element temp[MAX];
    for (int i = 0; i < size; i++) {
        temp[i] = pq[i];
    }

    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (temp[j].priority > temp[j + 1].priority) {
                Element t = temp[j];
                temp[j] = temp[j + 1];
                temp[j + 1] = t;
            }
        }
    }

    printf("Priority Queue (by values):\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", temp[i].data);
    }
    printf("\n");
}

int main() {
    int choice, value;

    while (1) {
        printf("\n--- Priority Queue Menu ---\n");
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                enqueue(value, value);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}
