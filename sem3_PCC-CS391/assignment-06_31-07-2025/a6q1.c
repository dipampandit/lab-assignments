// Fibonacci Series using Stack and Recursion

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

int fib(int n) {
    if (n <= 1) {
        push(n);
        return n;
    }
    int a = fib(n - 1);
    int b = fib(n - 2);
    int val = a + b;
    push(val);
    return val;
}

int main() {
    int n = 10;
    fib(n - 1);
    for (int i = 0; i <= top; i++)
        printf("%d ", stack[i]);
    return 0;
}
