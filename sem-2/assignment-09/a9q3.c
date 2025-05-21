#include <stdio.h>

int main() {
    int lower, upper, num, i, isPrime;

    // Input range
    printf("Enter the lower and upper range: ");
    scanf("%d %d", &lower, &upper);

    printf("Prime numbers between %d and %d are:\n", lower, upper);

    for(num = lower; num <= upper; num++) {  
        if (num < 2)
            continue;

        isPrime = 1;

        for(i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime)
            printf("%d ", num);
    }

    return 0;
}
