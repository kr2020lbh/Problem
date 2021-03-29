#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int power(int x) {
	int result = 1;
	for (int i = 0; i < x; i++) {
		result = result * 10;
	}
	return result;
}	

int solution(const char* s) {
	int len = strlen(s);
	int number_flag = 1;
	int answer = 0;
	int i = 0;
	if (s[0] == '+') {
		i++;
	}
	if (s[0] == '-') {
		number_flag = -1;
		i++;
	}

	for (i; i < len; i++) {
		answer = answer + (s[i] - 48)*number_flag * power(len - i - 1);
	}
	return answer;
}

int main() {
	printf("%d\n", solution("1234"));
	printf("%d\n", solution("+1234"));
	printf("%d\n", solution("-1234"));
	printf("%d", atoi("-12355"));
	printf("%d", atoi("+2355"));
	printf("%d", atoi("d12355"));
	return 0;
}