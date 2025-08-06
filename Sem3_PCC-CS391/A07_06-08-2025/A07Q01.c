// Postfix to Prefix

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

char stack[MAX][MAX];
int top = -1;

void push(char *str) {
    if (top >= MAX - 1) {
        printf("Stack Overflow!\n");
        exit(1);
    }
    strcpy(stack[++top], str);
}

char* pop() {
    if (top < 0) {
        printf("Stack Underflow!\n");
        exit(1);
    }
    return stack[top--];
}

int isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '%');
}

void postfixToPrefix(char* postfix) {
    char op1[MAX], op2[MAX], temp[MAX];
    int i;

    for (i = 0; postfix[i]; i++) {
        char ch = postfix[i];

        if (isspace(ch)) continue;

        if (isOperator(ch)) {
            if (top < 1) {
                printf("Invalid postfix expression (insufficient operands).\n");
                exit(1);
            }

            strcpy(op2, pop());
            strcpy(op1, pop());

            temp[0] = ch;
            temp[1] = '\0';
            strcat(temp, op1);
            strcat(temp, op2);

            push(temp);
        } else {
            char operand[2] = {ch, '\0'};
            push(operand);
        }
    }

    if (top != 0) {
        printf("Invalid postfix expression (extra operands).\n");
        exit(1);
    }

    printf("Prefix Expression: %s\n", pop());
}

int main() {
    char postfix[MAX];

    printf("Enter a postfix expression: ");
    fgets(postfix, MAX, stdin);

    postfixToPrefix(postfix);

    return 0;
}
