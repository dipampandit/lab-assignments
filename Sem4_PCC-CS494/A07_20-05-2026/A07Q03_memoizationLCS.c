// LCS using Memoization

#include <stdio.h>
#include <string.h>

int dp[100][100];

int max(int a, int b) {
    return (a > b) ? a : b;
}

int LCS(char X[], char Y[], int m, int n) {

    if(m == 0 || n == 0)
        return 0;

    if(dp[m][n] != -1)
        return dp[m][n];

    if(X[m-1] == Y[n-1])
        return dp[m][n] =
               1 + LCS(X,Y,m-1,n-1);

    return dp[m][n] =
           max(LCS(X,Y,m-1,n),
               LCS(X,Y,m,n-1));
}

int main() {

    memset(dp,-1,sizeof(dp));

    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";

    printf("LCS Length = %d",
           LCS(X,Y,strlen(X),strlen(Y)));

    return 0;
}