#include <stdio.h>

int main() {
    int num, sum = 0, count = 0;
    float avg;

    printf("Enter positive numbers (negative number to stop):\n");

    while (1) {
        scanf("%d", &num);
        if (num < 0)
            break;
        sum += num;
        count++;
    }

    if (count > 0)
        avg = (float)sum / count;
    else
        avg = 0;

    printf("Sum = %d\n", sum);
    printf("Average = %.2f\n", avg);

    return 0;
}
