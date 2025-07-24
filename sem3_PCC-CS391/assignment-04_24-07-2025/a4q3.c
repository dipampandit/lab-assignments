#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *arr;
    int top;
    int capacity;
} Stack;

Stack* createStack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->arr = (int*)malloc(capacity * sizeof(int));
    return stack;
}

int isFull(Stack *stack) {
    return stack->top == stack->capacity - 1;
}

int isEmpty(Stack *stack) {
    return stack->top == -1;
}

void push(Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack Overflow!\n");
        return;
    }
    stack->arr[++stack->top] = value;
    printf("Pushed: %d\n", value);
}

int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack Underflow!\n");
        return -1;
    }
    return stack->arr[stack->top--];
}

int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return stack->arr[stack->top];
}

void display(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = 0; i <= stack->top; i++)
        printf("%d ", stack->arr[i]);
    printf("\n");
}

void freeStack(Stack *stack) {
    free(stack->arr);
    free(stack);
}

int main() {
    int size, choice, value;
    printf("Enter stack capacity: ");
    scanf("%d", &size);

    Stack *stack = createStack(size);

    while (1) {
        printf("\nMenu:\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(stack, value);
                break;
            case 2:
                value = pop(stack);
                if (value != -1) printf("Popped: %d\n", value);
                break;
            case 3:
                value = peek(stack);
                if (value != -1) printf("Top element: %d\n", value);
                break;
            case 4:
                display(stack);
                break;
            case 5:
                freeStack(stack);
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice!\n");
        }
    }
}
