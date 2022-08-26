#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isSafeBridge(char bridge[]) {
    char *safe = strchr(bridge, ' ');
    return (safe == NULL) ? true : false;
}

int main() {
    // Run 
    bool ans = isSafeBridge("###");

    // 0 if not safe, 1 if safe
    printf("%i\n", ans);

    return 0;
}