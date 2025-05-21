#include <stdio.h>

struct Student {
    char *name;
    int roll;  
    float marks;
};

int main() {
    struct Student s;

    s.name = "Dipam";
    s.roll = 12345;
    s.marks = 91.75;

    printf("Student Structure Demo\n");
    printf("------------------------\n");
    printf("Name: %s\n", s.name);
    printf("Roll Number: %d\n", s.roll);
    printf("Total Marks: %.2f\n", s.marks);
    return 0;
}
