#include <stdio.h>

int main() {
    int a = 10, b = 20;
    
    (a > b) ? printf("a is greater\n") : (a < b) ? printf("b is greater\n") : printf("Both are equal\n");
    
    return 0;
}
