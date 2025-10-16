#include <stdio.h>
#include <stdlib.h>

#define ORDER 5

typedef struct BPlusNode {
    int keys[ORDER];
    struct BPlusNode* children[ORDER + 1];
    int count;
    int isLeaf;
    struct BPlusNode* next;
} BPlusNode;

BPlusNode* createNode(int isLeaf) {
    BPlusNode* node = (BPlusNode*)malloc(sizeof(BPlusNode));
    node->isLeaf = isLeaf;
    node->count = 0;
    node->next = NULL;
    for (int i = 0; i <= ORDER; i++)
        node->children[i] = NULL;
    return node;
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
}

void splitChild(BPlusNode* parent, int index, BPlusNode* child) {
    int mid = child->count / 2;
    BPlusNode* newChild = createNode(child->isLeaf);

    newChild->count = child->count - mid - 1;
    for (int i = 0; i < newChild->count; i++)
        newChild->keys[i] = child->keys[i + mid + 1];

    if (!child->isLeaf)
        for (int i = 0; i <= newChild->count; i++)
            newChild->children[i] = child->children[i + mid + 1];

    if (child->isLeaf) {
        newChild->count = child->count - mid;
        for (int i = 0; i < newChild->count; i++)
            newChild->keys[i] = child->keys[i + mid];
        child->count = mid;
        newChild->next = child->next;
        child->next = newChild;
    } else {
        child->count = mid;
    }

    for (int i = parent->count; i > index; i--) {
        parent->keys[i] = parent->keys[i - 1];
        parent->children[i + 1] = parent->children[i];
    }

    parent->keys[index] = child->keys[mid];
    parent->children[index + 1] = newChild;
    parent->count++;
}

void insertNonFull(BPlusNode* node, int key) {
    int i = node->count - 1;
    if (node->isLeaf) {
        while (i >= 0 && key < node->keys[i]) {
            node->keys[i + 1] = node->keys[i];
            i--;
        }
        node->keys[i + 1] = key;
        node->count++;
    } else {
        while (i >= 0 && key < node->keys[i]) i--;
        i++;
        if (node->children[i]->count == ORDER - 1) {
            splitChild(node, i, node->children[i]);
            if (key > node->keys[i])
                i++;
        }
        insertNonFull(node->children[i], key);
    }
}

void insert(BPlusNode** root, int key) {
    if (*root == NULL) {
        *root = createNode(1);
        (*root)->keys[0] = key;
        (*root)->count = 1;
        return;
    }

    if ((*root)->count == ORDER - 1) {
        BPlusNode* newRoot = createNode(0);
        newRoot->children[0] = *root;
        splitChild(newRoot, 0, *root);
        int i = (key > newRoot->keys[0]) ? 1 : 0;
        insertNonFull(newRoot->children[i], key);
        *root = newRoot;
    } else {
        insertNonFull(*root, key);
    }
}

void display(BPlusNode* root, int level) {
    if (root == NULL) return;

    printf("Level %d: ", level);
    for (int i = 0; i < root->count; i++)
        printf("%d ", root->keys[i]);
    printf("\n");

    if (!root->isLeaf)
        for (int i = 0; i <= root->count; i++)
            display(root->children[i], level + 1);
}

int main() {
    BPlusNode* root = NULL;
    int n, val;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter value %d: ", i + 1);
        scanf("%d", &val);
        insert(&root, val);
        printf("\n--- Tree after inserting %d ---\n", val);
        display(root, 0);
        printf("-------------------------------\n");
    }
    return 0;
}
