#include <stdio.h>
#include <math.h>

int main(void) {
    int n, i;
    float x, sum = 1.0, term, fact;
    
    printf("Enter value of x: ");
    scanf("%f", &x);
    
    printf("Enter number of terms (n): ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        fact = 1;
        for (int j = 1; j <= i; j++) {
            fact *= j;
        }
        term = pow(x, i) / fact;
        sum += term;
    }
    
    printf("Sum of the series = %.4f\n", sum);
    
    return 0;
}
