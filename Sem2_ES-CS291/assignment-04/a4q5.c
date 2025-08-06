#include <stdio.h>

int main(void) {
    int num, lower, upper;
    
    printf("Enter the lower limit: ");
    scanf("%d", &lower);
    
    printf("Enter the upper limit: ");
    scanf("%d", &upper);
    
    printf("Enter a number: ");
    scanf("%d", &num);
    
    if (num >= lower && num <= upper) {
        printf("%d is within the range [%d, %d]\n", num, lower, upper);
    } else {
        printf("%d is outside the range [%d, %d]\n", num, lower, upper);
    }
    
    return 0;
}
