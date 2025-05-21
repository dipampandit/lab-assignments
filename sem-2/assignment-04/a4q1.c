#include <stdio.h>

int main(void) {
    int dividend, divisor, remainder;
    
    printf("Enter Dividend: ");
    scanf("%d", &dividend);
    
    printf("Enter Divisor: ");
    scanf("%d", &divisor);
    
    remainder = dividend % divisor;
    
    printf("Remainder = %d\n", remainder);
    
    return 0;
}
