#include <stdio.h>
#include <math.h>

int main(void) {
    int n, i, num;
    
    printf("Enter number of elements: ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        printf("Enter number %d: ", i);
        scanf("%d", &num);
        printf("Square root = %.2f\n", sqrt(num));
    }
    
    return 0;
}
