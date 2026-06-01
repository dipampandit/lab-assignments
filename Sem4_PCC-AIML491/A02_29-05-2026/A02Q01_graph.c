#include <stdio.h>

int main() {
    int V, E;

    printf("Enter the number of vertices: ");
    scanf("%d", &V);

    int graph[V][V];

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            graph[i][j] = 0;
        }
    }

    printf("Enter the number of edges: ");
    scanf("%d", &E);

    for (int i = 1; i <= E; i++) {
        int S, D;
        printf("Enter the Source of the Edge (1 - %d): ", V);
        scanf("%d", &S);
        printf("Enter the Destination of the Edge (1 - %d): ", V);
        scanf("%d", &D);

        graph[S-1][D-1] = 1;
        graph[D-1][S-1] = 1;
    }

    printf("Adjacency Matrix:\n");
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
    return 0;
}