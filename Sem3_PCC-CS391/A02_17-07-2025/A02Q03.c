#include <stdio.h>

struct Employee {
    int id;
    char name[50];
    float salary;
};

// Function to display employees with salary > 50000
void displayHighSalary(struct Employee *e, int n) {
    printf("\nEmployees with salary > 50,000:\n");
    for (int i = 0; i < n; i++) {
        if ((e + i)->salary > 50000) {
            printf("ID: %d | Name: %s | Salary: %.2f\n", 
                   (e + i)->id, (e + i)->name, (e + i)->salary);
        }
    }
}

int main() {
    struct Employee emp[10];

    printf("Enter details of 10 employees:\n");
    for (int i = 0; i < 10; i++) {
        printf("\nEmployee %d:\n", i + 1);
        printf("ID: ");
        scanf("%d", &emp[i].id);
        printf("Name: ");
        scanf("%s", emp[i].name);
        printf("Salary: ");
        scanf("%f", &emp[i].salary);
    }

    displayHighSalary(emp, 10);

    return 0;
}
