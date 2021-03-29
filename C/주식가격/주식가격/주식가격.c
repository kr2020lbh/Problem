#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// prices_len은 배열 prices의 길이입니다.
int* solution(int prices[], size_t prices_len) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
	int* answer = (int*)malloc(sizeof(int) * prices_len);
	int i = 0;
	int j = 0;
	for (i; i < prices_len; i++) {
		for (j=i+1; j < prices_len; j++) {
			if (prices[j] < prices[i]) {
				break;
			}
		}
		if (j == prices_len) {
			answer[i] = j - i - 1;
		}
		else {
			answer[i] = j - i;
		}
	}
	return answer;
}

int main() {
	int numArr[5] = { 1, 2, 3, 2, 3 };
	solution(numArr, 5);
	return 0;
}