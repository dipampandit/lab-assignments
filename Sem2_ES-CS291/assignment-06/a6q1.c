#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    // Find the largest by comparing the difference
    int largest = a * (a >= b && a >= c) + b * (b >= a && b >= c) + c * (c >= a && c >= b);

    printf("The largest number is: %d\n", largest);

    return 0;
}
