#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
char* solution(const char* phone_number) {
    int len = strlen(phone_number);
    char* answer = (char*)malloc(sizeof(char)*len + 1);
    int i = 0;
    for (i; i < len; i++) {
        if (i < len - 4) {
            answer[i] = '*';
        }
        else {
            answer[i] = phone_number[i];
        }
    }
    answer[i] = NULL;
    return answer;
}

int main() {
    solution("01033334444");
    solution("4444");
    return 0;
}