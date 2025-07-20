#include <stdio.h>

int main() {
    int n, i = 0;
    float x, result = 1;
    
    printf("Enter the base (x): ");
    scanf("%f", &x);
    printf("Enter the exponent (n): ");
    scanf("%d", &n);

    while (i < n) {
        result *= x;
        i++;
    }

    printf("%.2f raised to the power %d is %.2f\n", x, n, result);
    return 0;
}
