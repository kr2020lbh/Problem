#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
bool solution(const char* s) {
    int len = strlen(s);
    if (len == 4 || len == 6) {
        for (int i = 0; i < len; i++) {
            if (s[i] >= 65) {
                return false;
            }
        }
    }
    else {
        return false;
    }
    return true;
}

int main() {
    solution("1234aAzZ");
    solution("1234aA");
    return 0;
}