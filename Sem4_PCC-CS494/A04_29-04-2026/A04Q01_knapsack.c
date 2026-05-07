// Implement 0/1 and fractional knapsack using suitable example and find maximum profit using greedy algorithm

#include <stdio.h>
#define ITEM 4

typedef struct {
    int weight;
    int profit;
    float ratio;
} Item;

// Sort items by profit/weight ratio (descending)
void sortItems(Item arr[]) {
    for (int i = 0; i < ITEM - 1; i++) {
        for (int j = 0; j < ITEM - i - 1; j++) {
            if (arr[j].ratio < arr[j + 1].ratio) {
                Item temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Fractional Knapsack
double fracKnapsack(Item items[], double capacity) {
    float fracProfit = 0.0;

    for (int i = 0; i < ITEM; i++) {
        if (items[i].weight <= capacity) {
            capacity -= items[i].weight;
            fracProfit += items[i].profit;
        } else {
            fracProfit += items[i].ratio * capacity;
            break;
        }
    }
    return fracProfit;
}

// 0/1 Knapsack
int zeroOneKnapsack(Item items[], int capacity) {
    int zeroOneProfit = 0;

    for (int i = 0; i < ITEM; i++) {
        if (items[i].weight <= capacity) {
            capacity -= items[i].weight;
            zeroOneProfit += items[i].profit;
        }
    }
    return zeroOneProfit;
}

int main() {
    int capacity = 5;

    Item items[ITEM] = {
        {2, 12, 0},
        {1, 10, 0},
        {3, 20, 0},
        {2, 15, 0}
    };

    // calculating ratio = profit / weight
    for (int i = 0; i < ITEM; i++) {
        items[i].ratio = (float)items[i].profit / items[i].weight;
    }

    // sorting items by ratio
    sortItems(items);

    // Output
    printf("Maximum Profit (Fractional Knapsack): %.2f\n", fracKnapsack(items, capacity));
    printf("Maximum Profit (0/1 Knapsack - Greedy): %d\n", zeroOneKnapsack(items, capacity));

    return 0;
}