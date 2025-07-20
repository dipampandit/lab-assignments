#include <stdio.h>

int main(void) {
    int n, i, count = 0;
    
    printf("Enter a number: ");
    scanf("%d", &n);
    
    if (n <= 1) {
        printf("Not a prime number.\n");
        return 0;
    }
    
    for (i = 2; i <= n/2; i++) {
        if (n % i == 0) {
            count = 1;
            break;
        }
    }
    
    if (count == 0)
        printf("Prime number.\n");
    else
        printf("Not a prime number.\n");
    
    return 0;
}
