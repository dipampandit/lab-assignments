#include <stdio.h>

int main(void) {
    char ch;
    
    printf("Enter a character: ");
    scanf(" %c", &ch); // Notice the space before %c
    
    printf("ASCII value of %c = %d\n", ch, ch);
    
    return 0;
}
