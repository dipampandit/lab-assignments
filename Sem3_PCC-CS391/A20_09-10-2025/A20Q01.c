#include <stdio.h>
#include <stdlib.h>

#define MIN_DEGREE 2

typedef struct BTreeNode {
    int *keys;
    int t;
    struct BTreeNode **C;
    int n;
    int leaf;
} BTreeNode;

BTreeNode *createNode(int t, int leaf);
void traverse(BTreeNode *root);
BTreeNode *insert(BTreeNode *root, int k);
void insertNonFull(BTreeNode *x, int k);
void splitChild(BTreeNode *x, int i, BTreeNode *y);
void bubbleSort(int arr[], int n);

BTreeNode *createNode(int t, int leaf) {
    BTreeNode *node = (BTreeNode *)malloc(sizeof(BTreeNode));
    node->t = t;
    node->leaf = leaf;
    node->keys = (int *)malloc(sizeof(int) * (2 * t - 1));
    node->C = (BTreeNode **)malloc(sizeof(BTreeNode *) * (2 * t));
    node->n = 0;
    return node;
}

void traverse(BTreeNode *root) {
    if (root != NULL) {
        int i;
        for (i = 0; i < root->n; i++) {
            if (!root->leaf)
                traverse(root->C[i]);
            printf("%d ", root->keys[i]);
        }
        if (!root->leaf)
            traverse(root->C[i]);
    }
}

BTreeNode *insert(BTreeNode *root, int k) {
    if (root == NULL) {
        root = createNode(MIN_DEGREE, 1);
        root->keys[0] = k;
        root->n = 1;
        return root;
    }

    if (root->n == 2 * MIN_DEGREE - 1) {
        BTreeNode *s = createNode(MIN_DEGREE, 0);
        s->C[0] = root;
        splitChild(s, 0, root);
        int i = 0;
        if (s->keys[0] < k)
            i++;
        insertNonFull(s->C[i], k);
        return s;
    } else {
        insertNonFull(root, k);
        return root;
    }
}

void insertNonFull(BTreeNode *x, int k) {
    int i = x->n - 1;
    if (x->leaf) {
        while (i >= 0 && x->keys[i] > k) {
            x->keys[i + 1] = x->keys[i];
            i--;
        }
        x->keys[i + 1] = k;
        x->n += 1;
    } else {
        while (i >= 0 && x->keys[i] > k)
            i--;
        i++;
        if (x->C[i]->n == 2 * MIN_DEGREE - 1) {
            splitChild(x, i, x->C[i]);
            if (x->keys[i] < k)
                i++;
        }
        insertNonFull(x->C[i], k);
    }
}

void splitChild(BTreeNode *x, int i, BTreeNode *y) {
    int t = y->t;
    BTreeNode *z = createNode(t, y->leaf);
    z->n = t - 1;

    for (int j = 0; j < t - 1; j++)
        z->keys[j] = y->keys[j + t];

    if (!y->leaf)
        for (int j = 0; j < t; j++)
            z->C[j] = y->C[j + t];

    y->n = t - 1;

    for (int j = x->n; j >= i + 1; j--)
        x->C[j + 1] = x->C[j];

    x->C[i + 1] = z;

    for (int j = x->n - 1; j >= i; j--)
        x->keys[j + 1] = x->keys[j];

    x->keys[i] = y->keys[t - 1];
    x->n += 1;
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void collect(BTreeNode *node, int flat[], int *count) {
    if (!node) return;
    for (int i = 0; i < node->n; i++) {
        if (!node->leaf) collect(node->C[i], flat, count);
        flat[(*count)++] = node->keys[i];
    }
    if (!node->leaf) collect(node->C[node->n], flat, count);
}

int main() {
    BTreeNode *root = NULL;
    int elements[] = {10, 20, 5, 6, 12, 30, 7, 17};
    int n = sizeof(elements) / sizeof(elements[0]);

    printf("Inserting elements and showing traversal after each:\n");
    for (int i = 0; i < n; i++) {
        root = insert(root, elements[i]);
        printf("\nAfter inserting %d:\n", elements[i]);
        traverse(root);
        printf("\n");
    }

    int flat[50], count = 0;

    collect(root, flat, &count);
    bubbleSort(flat, count);

    printf("\nSorted elements (Bubble Sort):\n");
    for (int i = 0; i < count; i++)
        printf("%d ", flat[i]);
    printf("\n");

    return 0;
}
