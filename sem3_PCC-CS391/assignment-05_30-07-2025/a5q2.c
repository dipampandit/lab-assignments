// Write a C program to check whether the parentheses in an expression are balanced or not.
// The program should support (), {}, and [] brackets.

#include <stdio.h>
#include <stdlib.h>

#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) {
    if (top == MAX - 1) {
        printf("Stack overflow\n");
        exit(1);
    }
    stack[++top] = c;
}

char pop() {
    if (top == -1)
        return '\0';
    return stack[top--];
}

char peek() {
    if (top == -1)
        return '\0';
    return stack[top];
}

int isMatchingPair(char open, char close) {
    return (open == '(' && close == ')') ||
           (open == '[' && close == ']') ||
           (open == '{' && close == '}');
}

int isBalanced(const char* expr) {
    char c;
    for (int i = 0; expr[i] != '\0'; i++) {
        c = expr[i];

        if (c == '(' || c == '[' || c == '{') {
            push(c);
        }
        else if (c == ')' || c == ']' || c == '}') {
            if (top == -1 || !isMatchingPair(pop(), c)) {
                return 0;
            }
        }
    }

    return top == -1;
}

int main() {
    char expr[MAX];

    printf("Enter an expression: ");
    scanf("%s", expr);

    if (isBalanced(expr))
        printf("Balanced\n");
    else
        printf("Not Balanced\n");

    return 0;
}
