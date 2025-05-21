#include <stdio.h>

int main(void) {
    int days, years, months;
    
    printf("Enter total number of days: ");
    scanf("%d", &days);
    
    years = days / 365;
    days = days % 365;
    
    months = days / 30;
    days = days % 30;
    
    printf("Years = %d\nMonths = %d\nDays = %d\n", years, months, days);
    
    return 0;
}
