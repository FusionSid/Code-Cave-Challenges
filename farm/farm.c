#include <stdio.h>

int animals(int chickens, int cows, int pigs);

int main() {
    int ans;

    ans = animals(2, 3, 5);
    printf("%i\n", ans);

    ans = animals(1, 2, 3);
    printf("%i\n", ans);

    ans = animals(5, 2, 8);
    printf("%i\n", ans);

    return 0;
}

int animals(int chickens, int cows, int pigs) {
    return (chickens * 2) + (cows * 4) + (pigs * 4);
}