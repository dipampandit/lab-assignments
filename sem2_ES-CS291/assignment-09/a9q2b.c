#include <stdio.h>
#include <math.h>

int main() {
    int lower, upper, num, originalNum, remainder, n, sum, temp;

    // Input range
    printf("Enter the lower and upper range: ");
    scanf("%d %d", &lower, &upper);

    printf("Armstrong numbers between %d and %d are:\n", lower, upper);

    for(num = lower; num <= upper; num++) {  
        originalNum = num;
        sum = 0;
        
        // Count number of digits
        temp = num;
        n = 0;
        while(temp > 0) {
            temp /= 10;
            n++;
        }

        // Calculate Armstrong sum
        temp = num;
        while(temp > 0) {
            remainder = temp % 10;
            sum += pow(remainder, n);
            temp /= 10;
        }

        // Check if Armstrong
        if(sum == originalNum) {
            printf("%d ", num);
        }
    }

    return 0;
}
