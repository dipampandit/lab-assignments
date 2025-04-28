#include <stdio.h>

int main() {
    int n, i = 1, j, termSum, totalSum = 0;
    
    printf("Enter the number of terms (n): ");
    scanf("%d", &n);

    while (i <= n) {
        termSum = 0;
        j = 1;
        while (j <= i) {
            termSum += j;
            j++;
        }
        totalSum += termSum;
        i++;
    }

    printf("The evaluated sum is %d\n", totalSum);
    return 0;
}
