#include <stdio.h>

#define SIZE 100

void insert(int arr[], int *n, int pos, int elem) {
    if(pos > *n || pos < 0) {
        printf("Invalid position!\n");
        return;
    }
    for(int i = *n; i > pos; i--) {
        arr[i] = arr[i - 1];
    }
    arr[pos] = elem;
    (*n)++;
}

void delete(int arr[], int *n, int pos) {
    if(pos >= *n || pos < 0) {
        printf("Invalid position!\n");
        return;
    }
    for(int i = pos; i < *n - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*n)--;
}

void display(int arr[], int n) {
    if(n == 0) {
        printf("Array is empty.\n");
        return;
    }
    printf("Array elements: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[SIZE], n = 0, choice, elem, pos;

    do {
        printf("\nMenu:\n");
        printf("1. Insert element at a position\n");
        printf("2. Delete element from a position\n");
        printf("3. Display array\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("Enter element and position: ");
                scanf("%d %d", &elem, &pos);
                insert(arr, &n, pos, elem);
                break;
            case 2:
                printf("Enter position to delete: ");
                scanf("%d", &pos);
                delete(arr, &n, pos);
                break;
            case 3:
                display(arr, n);
                break;
            case 4:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while(choice != 4);

    return 0;
}
