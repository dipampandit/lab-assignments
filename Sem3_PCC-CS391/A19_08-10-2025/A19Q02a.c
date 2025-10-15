/* 
Implement Binary Tree using Recursion in Array.
*/

#include <stdio.h>

#define MAX 100

int tree[MAX];

void initTree() {
    for (int i = 0; i < MAX; i++)
        tree[i] = -1;
}

void insert(int index, int value) {
    if (index >= MAX) {
        printf("Tree overflow.\n");
        return;
    }
    if (tree[index] == -1) {
        tree[index] = value;
    } else {
        int ch;
        printf("Node %d already exists. Insert left(1) or right(2) of %d: ", tree[index], tree[index]);
        scanf("%d", &ch);
        if (ch == 1)
            insert(2 * index + 1, value);
        else
            insert(2 * index + 2, value);
    }
}

void inorder(int index) {
    if (index < MAX && tree[index] != -1) {
        inorder(2 * index + 1);
        printf("%d ", tree[index]);
        inorder(2 * index + 2);
    }
}

int main() {
    int choice, value;
    initTree();

    while (1) {
        printf("\n--- Binary Tree using Recursion (Array Representation) ---\n");
        printf("1. Insert\n2. Display (Inorder)\n3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                if (tree[0] == -1)
                    tree[0] = value;
                else
                    insert(0, value);
                break;

            case 2:
                printf("Inorder traversal: ");
                inorder(0);
                printf("\n");
                break;

            case 3:
                return 0;

            default:
                printf("Invalid choice.\n");
        }
    }
}
