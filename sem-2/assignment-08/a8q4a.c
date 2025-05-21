#include <stdio.h>
#include <math.h>

int main(void) {
    int n, i = 1, num;
    
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    start:
        if (i <= n) {
            printf("Enter number %d: ", i);
            scanf("%d", &num);
            printf("Square root = %.2f\n", sqrt(num));
            i++;
            goto start;
        }
    
    return 0;
}
