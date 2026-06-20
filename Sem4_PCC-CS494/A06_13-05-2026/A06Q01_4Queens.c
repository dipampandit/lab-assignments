// Find all possible solutions of 4 queen problem using backtracking algorithm.

#include <stdio.h>
#include <stdbool.h>

#define N 4

int count = 0;

void printBoard(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j])
                printf("Q ");
            else
                printf(". ");
        }
        printf("\n");
    }
    printf("\n");
}

bool isSafe(int board[N][N], int row, int col) {
    int i, j;

    // Check column
    for (i = 0; i < row; i++) {
        if (board[i][col])
            return false;
    }

    // Upper-left diagonal
    for (i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j])
            return false;
    }

    // Upper-right diagonal
    for (i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++) {
        if (board[i][j])
            return false;
    }

    return true;
}

void solveNQueens(int board[N][N], int row) {
    if (row == N) {
        count++;
        printf("Solution %d:\n", count);
        printBoard(board);
        return;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 1;

            solveNQueens(board, row + 1);

            // Backtrack
            board[row][col] = 0;
        }
    }
}

int main() {
    int board[N][N] = {0};

    solveNQueens(board, 0);

    printf("Total solutions = %d\n", count);

    return 0;
}