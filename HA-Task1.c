//Pascal's Triangle code

#include <stdio.h>

void printPascalsTriangle(int n) {
    for (int line = 0; line < n; line++) {
        int num = 1;
//The first element of every line is always 1

//Print leading spaces for alignment (optional)
        for (int space = 0; space < n - line - 1; space++) {
            printf(" ");
        }

//Print each number in the current line
        for (int i = 0; i <= line; i++) {
            printf("%d ", num);
            num = num * (line - i) / (i + 1);
        }
        printf("\n");
    }
}

int main() {
    int n;

    printf("Enter the number of rows for Pascal's Triangle: ");
    scanf("%d", &n);

    printPascalsTriangle(n);
    
    return 0;
}