#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// prices_len�� �迭 prices�� �����Դϴ�.
int* solution(int prices[], size_t prices_len) {
	// return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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