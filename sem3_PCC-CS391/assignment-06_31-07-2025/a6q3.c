// Postfix Evaluation using Stack and Recursion

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int val) {
    if (top >= MAX - 1) {
        printf("Stack Overflow\n");
        exit(1);
    }
    stack[++top] = val;
}

int pop() {
    if (top < 0) {
        printf("Stack Underflow\n");
        exit(1);
    }
    return stack[top--];
}

void evaluatePostfix(char *expr, int index) {
    if (index < 0) return;

    char ch = expr[index];

    evaluatePostfix(expr, index - 1);

    if (isdigit(ch)) {
        push(ch - '0');
    } else {
        int a = pop();
        int b = pop();
        int res;

        switch (ch) {
            case '+': res = b + a; break;
            case '-': res = b - a; break;
            case '*': res = b * a; break;
            case '/': 
                if (a == 0) {
                    printf("Division by zero!\n");
                    exit(1);
                }
                res = b / a; 
                break;
            default:
                printf("Invalid operator: %c\n", ch);
                exit(1);
        }

        push(res);
    }
}

int main() {
    char postfixExpr[MAX];

    printf("Enter postfix expression: ");
    scanf("%s", postfixExpr);

    int len = strlen(postfixExpr);
    evaluatePostfix(postfixExpr, len - 1);
    printf("Result: %d\n", pop());

    return 0;
}
