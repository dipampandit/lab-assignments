#include <stdio.h>

int main(void) {
    int a, b, c, d;
    float ratio;
    
    printf("Enter values for a, b: ");
    scanf("%d%d", &a, &b);
    
    printf("Enter values for c, d: ");
    scanf("%d%d", &c, &d);
    
    int numerator = a + b;
    int denominator = c + d;
    
    if (denominator != 0) {
        ratio = (float)numerator / denominator;
        printf("Ratio = %.2f\n", ratio);
    } else {
        printf("Denominator is zero. Cannot divide.\n");
    }
    
    return 0;
}
