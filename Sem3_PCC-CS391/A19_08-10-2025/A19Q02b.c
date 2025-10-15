/* 
Implement Binary Tree using Recursion in Linked List.
*/

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

void insert(struct Node** root, int data) {
    if (*root == NULL) {
        *root = createNode(data);
        return;
    }

    int ch;
    printf("Insert left(1) or right(2) of %d: ", (*root)->data);
    scanf("%d", &ch);

    if (ch == 1)
        insert(&((*root)->left), data);
    else
        insert(&((*root)->right), data);
}

void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

int main() {
    struct Node* root = NULL;
    int choice, value;

    while (1) {
        printf("\n--- Binary Tree using Recursion (Linked List Representation) ---\n");
        printf("1. Insert\n2. Display (Inorder)\n3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(&root, value);
                break;

            case 2:
                printf("Inorder traversal: ");
                inorder(root);
                printf("\n");
                break;

            case 3:
                exit(0);

            default:
                printf("Invalid choice.\n");
        }
    }
    return 0;
}
