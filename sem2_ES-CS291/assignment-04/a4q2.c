#include <stdio.h>

int main(void) {
    float num1, num2, num3, average;
    
    printf("Enter three numbers: ");
    scanf("%f%f%f", &num1, &num2, &num3);
    
    average = (num1 + num2 + num3) / 3.0;
    
    printf("Average = %.2f\n", average);
    
    return 0;
}
