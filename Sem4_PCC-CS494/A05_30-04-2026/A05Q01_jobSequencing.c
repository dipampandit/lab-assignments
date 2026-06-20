// Implement job sequencing with deadline problem using suitable example. Use greedy approach to find the maximum profit.

#include <stdio.h>
#define JOB 6

typedef struct {
    int profit;
    int deadline;
} Job;

void sortJobs(Job arr[]) {
    for (int i = 0; i < JOB - 1; i++) {
        for (int j = 0; j < JOB - i - 1; j++) {
            if (arr[j].profit < arr[j + 1].profit) {
                Job temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    Job jobs[JOB] = {
        {300, 4},
        {250, 2},
        {130, 3},
        {212, 3},
        {100, 3},
        {424, 3}
    };

    sortJobs(jobs);

    int maxDeadline = 0;

    for (int i = 0; i < JOB; i++) {
        if (jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;
    }

    int slot[maxDeadline];

    // Initialize slots as empty
    for (int i = 0; i < maxDeadline; i++)
        slot[i] = -1;

    int totalProfit = 0;

    // Schedule jobs greedily
    for (int i = 0; i < JOB; i++) {
        for (int j = jobs[i].deadline - 1; j >= 0; j--) {
            if (slot[j] == -1) {
                slot[j] = i;
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    printf("Selected Jobs:\n");
    for (int i = 0; i < maxDeadline; i++) {
        if (slot[i] != -1) {
            printf("Slot %d -> Profit = %d, Deadline = %d\n", i + 1, jobs[slot[i]].profit, jobs[slot[i]].deadline);
        }
    }

    printf("\nMaximum Profit = %d\n", totalProfit);

    return 0;
}