#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define _CRT_NONSTDC_NO_DEPRECATE

int* solution(long long n) {
	// 리턴할 값은 메모리를 동적 할당해주세요.
	int* answer = (int*)malloc(sizeof(int)*100);
	int i = 0;
	while (n) {
		answer[i] = n % 10;
		n /= 10 ;
		i++;
	}
	printf("%s\n", answer);
	return answer;
}


int main() {
	solution(10000);

	return 0;
}