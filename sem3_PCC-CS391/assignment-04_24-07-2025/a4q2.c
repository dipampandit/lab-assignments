#include <stdio.h>
#include <stdlib.h>

int *stack;
int top = -1;
int capacity; // size of stack decided at runtime

void push() {
    if (top == capacity - 1) {
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
    printf("Enter size of stack: ");
    scanf("%d", &capacity);

    // allocate memory dynamically
    stack = (int*) malloc(capacity * sizeof(int));

    if (stack == NULL) {
        printf("Memory allocation failed! Exiting...\n");
        return 1;
    }

    while (1) {
        printf("\n\n--- Stack Menu (Dynamic Array) ---\n");
        printf("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: peek(); break;
            case 4: display(); break;
            case 5: 
                free(stack);  // free allocated memory
                exit(0);
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}
