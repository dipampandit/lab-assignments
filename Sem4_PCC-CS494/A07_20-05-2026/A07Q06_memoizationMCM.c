// Matrix Chain Multiplication using Memoization

#include <stdio.h>
#include <string.h>
#include <limits.h>

int dp[100][100];

int min(int a, int b) {
    return (a < b) ? a : b;
}

int MCM(int arr[], int i, int j) {

    if(i == j)
        return 0;

    if(dp[i][j] != -1)
        return dp[i][j];

    dp[i][j] = INT_MAX;

    for(int k=i;k<j;k++) {

        int temp =
            MCM(arr,i,k) +
            MCM(arr,k+1,j) +
            arr[i-1]*arr[k]*arr[j];

        dp[i][j] = min(dp[i][j], temp);
    }

    return dp[i][j];
}

int main() {

    memset(dp,-1,sizeof(dp));

    int arr[] = {1,2,3,4,3};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Minimum Cost = %d",
           MCM(arr,1,n-1));

    return 0;
}