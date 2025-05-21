#include <stdio.h>

int main() {
    int a = 10, b = 20;
    
    if ((a > b) && (a != b))
        printf("a is greater\n");
    else if ((b > a) && (b != a))
        printf("b is greater\n");
    else
        printf("Both are equal\n");
    
    return 0;
}
