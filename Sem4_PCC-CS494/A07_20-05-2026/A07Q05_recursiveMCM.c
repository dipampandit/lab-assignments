// Matrix Chain Multiplication using Recursion

#include <stdio.h>
#include <limits.h>

int min(int a, int b) {
    return (a < b) ? a : b;
}

int MCM(int arr[], int i, int j) {

    if(i == j)
        return 0;

    int ans = INT_MAX;

    for(int k=i;k<j;k++) {

        int temp =
            MCM(arr,i,k) +
            MCM(arr,k+1,j) +
            arr[i-1]*arr[k]*arr[j];

        ans = min(ans,temp);
    }

    return ans;
}

int main() {

    int arr[] = {1,2,3,4,3};
    int n = sizeof(arr)/sizeof(arr[0]);

    printf("Minimum Cost = %d",
           MCM(arr,1,n-1));

    return 0;
}