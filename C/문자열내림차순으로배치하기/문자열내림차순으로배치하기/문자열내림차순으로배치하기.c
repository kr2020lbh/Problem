#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
char* solution(const char* s) {
    // return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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