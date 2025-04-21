#include <stdio.h>

int main() {
    int a, b, c, d;
    int gcd, lcm;
    int i, max;

    printf("Enter four numbers: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);

    // Find GCD
    int min = a;
    if(b < min) min = b;
    if(c < min) min = c;
    if(d < min) min = d;

    for(i = min; i >= 1; i--) {
        if(a % i == 0 && b % i == 0 && c % i == 0 && d % i == 0) {
            gcd = i;
            break;
        }
    }

    // Find LCM
    max = a;
    if(b > max) max = b;
    if(c > max) max = c;
    if(d > max) max = d;

    i = max;
    while(1) {
        if(i % a == 0 && i % b == 0 && i % c == 0 && i % d == 0) {
            lcm = i;
            break;
        }
        i++;
    }

    printf("GCD = %d\n", gcd);
    printf("LCM = %d\n", lcm);

    return 0;
}
