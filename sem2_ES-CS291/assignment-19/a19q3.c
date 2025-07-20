#include <stdio.h>

struct Rectangle {
    float length;
    float width;
};

// Function to calculate area
float calculateArea(struct Rectangle r) {
    return r.length * r.width;
}

// Function to calculate perimeter
float calculatePerimeter(struct Rectangle r) {
    return 2 * (r.length + r.width);
}

int main() {
    struct Rectangle r;

    r.length = 8.5;
    r.width = 4.2;

    printf("Rectangle Structure Demo\n");
    printf("--------------------------\n");
    printf("Length: %.2f\n", r.length);
    printf("Width: %.2f\n", r.width);
    printf("Area: %.2f\n", calculateArea(r));
    printf("Perimeter: %.2f\n", calculatePerimeter(r));

    return 0;
}
