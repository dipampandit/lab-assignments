#include <stdio.h>

struct Student {
    char name[50];
    float marks;
    char gender;
};

int main() {
    struct Student s;

    printf("Enter student name: ");
    scanf("%s", s.name);

    printf("Enter marks: ");
    scanf("%f", &s.marks);

    printf("Enter gender (M/F): ");
    scanf(" %c", &s.gender);  // Note the space before %c to consume newline

    printf("\nStudent Details:\n");
    printf("Name: %s\n", s.name);
    printf("Marks: %.2f\n", s.marks);
    printf("Gender: %c\n", s.gender);

    return 0;
}
