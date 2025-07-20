#include <stdio.h>

struct Student {
    char name[50];
    int age;
    int eng, math, dbms;
    int total;
};

// Function to calculate total marks
int calculateTotal(struct Student s) {
    return s.eng + s.math + s.dbms;
}

// Function to find student with highest marks
struct Student findTopper(struct Student s[], int n) {
    int maxIndex = 0;
    for (int i = 1; i < n; i++) {
        if (s[i].total > s[maxIndex].total) {
            maxIndex = i;
        }
    }
    return s[maxIndex];
}

int main() {
    struct Student students[10];

    printf("Enter details of 10 students:\n");
    for (int i = 0; i < 10; i++) {
        printf("\nStudent %d:\n", i + 1);
        printf("Name: ");
        scanf("%s", students[i].name);
        printf("Age: ");
        scanf("%d", &students[i].age);
        printf("Marks (Eng Math DBMS): ");
        scanf("%d %d %d", &students[i].eng, &students[i].math, &students[i].dbms);
        students[i].total = calculateTotal(students[i]);
    }

    struct Student topper = findTopper(students, 10);

    printf("\nStudent with Highest Marks:\n");
    printf("Name: %s\nAge: %d\nTotal Marks: %d\n", topper.name, topper.age, topper.total);

    return 0;
}
