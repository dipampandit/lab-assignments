#include <stdio.h>
#include <stdlib.h>

#define MAX 5

int stack[MAX];
int top = -1;

void push() {
    if (top == MAX - 1) {
        printf("\nStack Overflow! Cannot push.\n");
    } else {
        int value;
        printf("Enter value to push: ");
        scanf("%d", &value);
        stack[++top] = value;
        printf("%d pushed successfully.\n", value);
    }
}

void pop() {
    if (top == -1) {
        printf("\nStack Underflow! Nothing to pop.\n");
    } else {
        printf("Popped: %d\n", stack[top--]);
    }
}

void peek() {
    if (top == -1) {
        printf("\nStack is empty.\n");
    } else {
        printf("Top element: %d\n", stack[top]);
    }
}

void display() {
    if (top == -1) {
        printf("\nStack is empty.\n");
    } else {
        printf("\nStack elements: ");
        for (int i = top; i >= 0; i--) {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

int main() {
    int choice;
    while (1) {
        printf("\n\n--- Stack Menu ---\n");
        printf("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: peek(); break;
            case 4: display(); break;
            case 5: exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
