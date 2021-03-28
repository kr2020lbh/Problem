#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = strlen(s);
    int i = 0;
    char* answer = (char*)malloc(sizeof(char) * len + 1);
    for (i; i < len; i++) {
        answer[i] = s[i];
    }
    answer[i] = NULL;

    i = 0;
    for (i; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            if (answer[i] < answer[j]) {
                char temp = answer[i];
                answer[i] = answer[j];
                answer[j] = temp;
            }
        }
    }
    return answer;
}