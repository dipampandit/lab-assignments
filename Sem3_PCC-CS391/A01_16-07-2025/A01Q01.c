#include <stdio.h>
#define MAX 20

void insertElement(int arr[], int *n);
void deleteElement(int arr[], int *n);
void displayArray(int arr[], int n);

int main() {
    int arr[MAX], n = 0, choice;

    do {
        printf("1. Insert Element\n");
        printf("2. Delete Element\n");
        printf("3. Display Array\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                insertElement(arr, &n);
                break;
            case 2:
                deleteElement(arr, &n);
                break;
            case 3:
                displayArray(arr, n);
                break;
            case 4:
                printf("Exiting program...\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    } while (choice != 4);

    return 0;
}

void insertElement(int arr[], int *n) {
    if (*n >= MAX) {
        printf("Array is full! Cannot insert.\n");
        return;
    }

    int pos, value;
    printf("Enter position (0 to %d): ", *n);
    scanf("%d", &pos);
    printf("Enter value: ");
    scanf("%d", &value);

    if (pos < 0 || pos > *n) {
        printf("Invalid position!\n");
        return;
    }

    // shift elements right
    for (int i = *n; i > pos; i--) {
        arr[i] = arr[i - 1];
    }

    arr[pos] = value;
    (*n)++;
    printf("Element inserted successfully!\n");
}

void deleteElement(int arr[], int *n) {
    if (*n == 0) {
        printf("Array is empty! Nothing to delete.\n");
        return;
    }

    int pos;
    printf("Enter position to delete (0 to %d): ", *n - 1);
    scanf("%d", &pos);

    if (pos < 0 || pos >= *n) {
        printf("Invalid position!\n");
        return;
    }

    // shift elements left
    for (int i = pos; i < *n - 1; i++) {
        arr[i] = arr[i + 1];
    }

    (*n)--;
    printf("Element deleted successfully!\n");
}

void displayArray(int arr[], int n) {
    if (n == 0) {
        printf("Array is empty!\n");
        return;
    }

    printf("Array elements: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
