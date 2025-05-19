#include <stdio.h>

#define SIZE 100

void insert(int arr[], int *n, int pos, int val) {
    if (pos < 0 || pos > *n || *n >= SIZE) {
        printf("Invalid position or array full!\n");
        return;
    }
    for (int i = *n; i > pos; i--)
        arr[i] = arr[i - 1];
    arr[pos] = val;
    (*n)++;
}

void delete(int arr[], int *n, int pos) {
    if (pos < 0 || pos >= *n) {
        printf("Invalid position!\n");
        return;
    }
    for (int i = pos; i < *n - 1; i++)
        arr[i] = arr[i + 1];
    (*n)--;
}

void display(int arr[], int n) {
    if (n == 0) {
        printf("Array is empty.\n");
        return;
    }
    printf("Array elements: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[SIZE], n = 0, choice, pos, val;

    while (1) {
        printf("\nMenu:\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter position to insert (0-based): ");
                scanf("%d", &pos);
                printf("Enter value: ");
                scanf("%d", &val);
                insert(arr, &n, pos, val);
                break;
            case 2:
                printf("Enter position to delete (0-based): ");
                scanf("%d", &pos);
                delete(arr, &n, pos);
                break;
            case 3:
                display(arr, n);
                break;
            case 4:
                return 0;
            default:
                printf("Invalid choice.\n");
        }
    }
}
