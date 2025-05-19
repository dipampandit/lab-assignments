#include <stdio.h>

int factorial(int n) {
    if (n == 0 || n == 1) return 1;
    else return n * factorial(n - 1);
}

int main() {
    int numbers[] = {3, 4, 5};

    for (int i = 0; i < 3; i++) {
        printf("Factorial of %d is %d\n", numbers[i], factorial(numbers[i]));
    }
    return 0;
}
