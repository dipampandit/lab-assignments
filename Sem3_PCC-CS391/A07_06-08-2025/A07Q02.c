// Prefix Evaluation

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100

int stack[MAX];
int top = -1;

void push(int val) {
    if (top >= MAX - 1) {
        printf("Stack Overflow!\n");
        exit(1);
    }
    stack[++top] = val;
}

int pop() {
    if (top < 0) {
        printf("Stack Underflow!\n");
        exit(1);
    }
    return stack[top--];
}

int evaluatePrefix(char* expr) {
    int len = strlen(expr);

    for (int i = len - 1; i >= 0; i--) {
        char ch = expr[i];

        if (isspace(ch)) continue;

        if (isdigit(ch)) {
            push(ch - '0');
        } else if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '%') {
            if (top < 1) {
                printf("Invalid prefix expression (insufficient operands).\n");
                exit(1);
            }

            int op1 = pop();
            int op2 = pop();

            switch (ch) {
                case '+': push(op1 + op2); break;
                case '-': push(op1 - op2); break;
                case '*': push(op1 * op2); break;
                case '/':
                    if (op2 == 0) {
                        printf("Division by zero error!\n");
                        exit(1);
                    }
                    push(op1 / op2); break;
                case '%':
                    if (op2 == 0) {
                        printf("Modulo by zero error!\n");
                        exit(1);
                    }
                    push(op1 % op2); break;
            }
        } else {
            printf("Invalid character encountered: %c\n", ch);
            exit(1);
        }
    }

    if (top != 0) {
        printf("Invalid prefix expression (extra operands).\n");
        exit(1);
    }

    return pop();
}

int main() {
    char prefix[MAX];

    printf("Enter a prefix expression: ");
    fgets(prefix, MAX, stdin);

    int result = evaluatePrefix(prefix);
    printf("Result of Prefix Expression: %d\n", result);

    return 0;
}
