// 15 Puzzle Problem using Branch and Bound

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define N 4

typedef struct Node {
    int mat[N][N];
    int x, y;
    int cost;
    int level;
    struct Node *parent;
} Node;

int goal[N][N] = {
    {1,2,3,4},
    {5,6,7,8},
    {9,10,11,12},
    {13,14,15,0}
};

int row[] = {1,0,-1,0};
int col[] = {0,-1,0,1};

int calculateCost(int mat[N][N]) {
    int count = 0;
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            if(mat[i][j] && mat[i][j] != goal[i][j])
                count++;
    return count;
}

int isSafe(int x, int y) {
    return (x>=0 && x<N && y>=0 && y<N);
}

Node* newNode(int mat[N][N], int x, int y,
              int newX, int newY,
              int level, Node *parent) {

    Node *node = (Node*)malloc(sizeof(Node));

    memcpy(node->mat, mat, sizeof(node->mat));

    int temp = node->mat[x][y];
    node->mat[x][y] = node->mat[newX][newY];
    node->mat[newX][newY] = temp;

    node->parent = parent;
    node->x = newX;
    node->y = newY;
    node->level = level;
    node->cost = calculateCost(node->mat);

    return node;
}

void printMatrix(int mat[N][N]) {
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++)
            printf("%2d ", mat[i][j]);
        printf("\n");
    }
    printf("\n");
}

void printPath(Node *root) {
    if(root == NULL)
        return;

    printPath(root->parent);
    printMatrix(root->mat);
}

void solve(int initial[N][N], int x, int y) {

    Node *root = newNode(initial,x,y,x,y,0,NULL);

    if(root->cost == 0) {
        printPath(root);
        return;
    }

    printf("Initial Cost = %d\n", root->cost);
}

int main() {

    int initial[N][N] = {
        {1,2,3,4},
        {5,6,0,8},
        {9,10,7,12},
        {13,14,11,15}
    };

    solve(initial,1,2);

    return 0;
}