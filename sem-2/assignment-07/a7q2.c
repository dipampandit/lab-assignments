#include <stdio.h>

int main() {
    int n, i = 1, sum = 0;
    
    printf("Enter the value of n: ");
    scanf("%d", &n);

    while (i <= n) {
        sum += i * i;
        i++;
    }

    printf("Sum of squares up to %d is %d\n", n, sum);
    return 0;
}
