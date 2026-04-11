// Implement Tower of Hanoi 

#include <stdio.h>

void towerOfHanoi(int disc, char from, char to, char aux) {
    if (disc == 1) {
        printf("%c -> %c\n", from, to);
        return;
    }

    towerOfHanoi(disc - 1, from, aux, to);
    printf("%c -> %c\n", from, to);
    towerOfHanoi(disc - 1, aux, to, from);
}

int main() {
    int disc;
    printf("Enter the number of discs: ");
    scanf("%d", &disc);

    towerOfHanoi(disc, 'A', 'C', 'B');

    return 0;
}