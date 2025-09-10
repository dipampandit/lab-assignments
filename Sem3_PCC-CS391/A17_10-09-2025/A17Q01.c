/*
Q: Implement Binary Tree using Array.
   Display tree traversals: Preorder, Inorder, and Postorder.
*/

#include <stdio.h>
#define MAX 100

int tree[MAX];

void insertArray(int index, int value) {
    if (index >= MAX) {
        printf("Index out of range\n");
        return;
    }
    tree[index] = value;
}

void preorderArray(int index) {
    if (index >= MAX || tree[index] == 0) return;
    printf("%d ", tree[index]);
    preorderArray(2 * index + 1);
    preorderArray(2 * index + 2);
}

void inorderArray(int index) {
    if (index >= MAX || tree[index] == 0) return;
    inorderArray(2 * index + 1);
    printf("%d ", tree[index]);
    inorderArray(2 * index + 2);
}

void postorderArray(int index) {
    if (index >= MAX || tree[index] == 0) return;
    postorderArray(2 * index + 1);
    postorderArray(2 * index + 2);
    printf("%d ", tree[index]);
}

int main() {
    printf("Binary Tree using Array:\n");

    insertArray(0, 1);
    insertArray(1, 2);
    insertArray(2, 3);
    insertArray(3, 4);
    insertArray(4, 5);

    printf("Preorder: ");
    preorderArray(0);
    printf("\n");

    printf("Inorder: ");
    inorderArray(0);
    printf("\n");

    printf("Postorder: ");
    postorderArray(0);
    printf("\n");

    return 0;
}
