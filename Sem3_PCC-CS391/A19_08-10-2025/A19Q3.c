/*
Implement One-Way Threaded Binary Tree.
*/

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
    int rightThread;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    newNode->rightThread = 1;
    return newNode;
}

struct Node* insert(struct Node* root, int data) {
    struct Node* ptr = root;
    struct Node* parent = NULL;

    while (ptr != NULL) {
        if (data == ptr->data) {
            printf("Duplicate data not allowed.\n");
            return root;
        }

        parent = ptr;

        if (data < ptr->data) {
            if (ptr->left == NULL)
                break;
            else
                ptr = ptr->left;
        } else {
            if (ptr->rightThread == 0)
                ptr = ptr->right;
            else
                break;
        }
    }

    struct Node* newNode = createNode(data);

    if (parent == NULL)
        root = newNode;
    else if (data < parent->data) {
        newNode->left = NULL;
        newNode->right = parent;
        parent->left = newNode;
    } else {
        newNode->right = parent->right;
        parent->right = newNode;
        parent->rightThread = 0;
    }

    return root;
}

void inorder(struct Node* root) {
    struct Node* ptr = root;

    if (root == NULL) {
        printf("Tree is empty.\n");
        return;
    }

    while (ptr->left != NULL)
        ptr = ptr->left;

    while (ptr != NULL) {
        printf("%d ", ptr->data);
        if (ptr->rightThread == 1)
            ptr = ptr->right;
        else {
            ptr = ptr->right;
            while (ptr != NULL && ptr->left != NULL)
                ptr = ptr->left;
        }
    }
}

int main() {
    struct Node* root = NULL;
    int choice, value;

    while (1) {
        printf("\n--- One-Way Threaded Binary Tree ---\n");
        printf("1. Insert\n2. Display (Inorder)\n3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                root = insert(root, value);
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
}
