// Factorial using Stack and Recursion

#include <stdio.h>

#define MAX 100

int stack[MAX], top = -1;

int isFull() {
    return top == MAX - 1;
}

int isEmpty() {
    return top == -1;
}

void push(int x) {
    if (isFull()) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = x;
}

int fact(int n) {
    if (n == 0) {
        push(1);
        return 1;
    }
    int res = n * fact(n - 1);
    push(res);
    return res;
}

int main() {
    int n = 5;
    fact(n);
    for (int i = 0; i <= top; i++)
        printf("%d ", stack[i]);
    return 0;
}
