#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int isArmstrong(int n) {
    int sum = 0, temp = n, digits = 0;
    while (temp) {
        digits++;
        temp /= 10;
    }
    temp = n;
    while (temp) {
        int digit = temp % 10;
        sum += pow(digit, digits);
        temp /= 10;
    }
    return sum == n;
}

int isPerfect(int n) {
    int sum = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0)
            sum += i;
    }
    return sum == n;
}

int main() {
    int start, end;
    printf("Enter the range (start and end): ");
    scanf("%d %d", &start, &end);

    printf("\nPrime numbers in range:\n");
    for (int i = start; i <= end; i++) {
        if (isPrime(i))
            printf("%d ", i);
    }

    printf("\n\nArmstrong numbers in range:\n");
    for (int i = start; i <= end; i++) {
        if (isArmstrong(i))
            printf("%d ", i);
    }

    printf("\n\nPerfect numbers in range:\n");
    for (int i = start; i <= end; i++) {
        if (isPerfect(i))
            printf("%d ", i);
    }

    printf("\n");
    return 0;
}
