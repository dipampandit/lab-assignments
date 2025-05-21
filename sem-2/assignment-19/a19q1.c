#include <stdio.h>

int main() {
    int var = 100;
    int *ptr = &var;
    int **pptr = &ptr;

    printf("Pointer to Pointer Demo\n");
    printf("Address of ptr (using pptr): %p\n", (void*)pptr);
    printf("Value of var (using pptr): %d\n", **pptr);
    return 0;
}
