#include <stdio.h>

int main(void) {
    int n, temp, sum = 0, reverse = 0, rem;
    
    printf("Enter a number: ");
    scanf("%d", &n);
    
    temp = n;
    
    while (temp > 0) {
        rem = temp % 10;
        sum += rem;
        reverse = reverse * 10 + rem;
        temp /= 10;
    }
    
    printf("Sum of digits = %d\n", sum);
    
    if (n == reverse)
        printf("The number is a palindrome.\n");
    else
        printf("The number is not a palindrome.\n");
        
    return 0;
}
