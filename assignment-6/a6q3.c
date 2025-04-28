#include <stdio.h>

int main(void) {
    float base, height, area;
    
    printf("Enter base and height of the triangle: ");
    scanf("%f%f", &base, &height);
    
    area = (base * height) / 2;
    
    printf("Area of the triangle = %.2f\n", area);
    
    return 0;
}
