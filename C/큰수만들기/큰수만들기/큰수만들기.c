#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* number, int k) {
	// return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
	int number_len = strlen(number);
	int idx = 0;
	char* answer = (char*)malloc(sizeof(char)*(number_len-k));
	int start = -1;
	for (int i = k; i < number_len; i++) {
		int new_start=i;
		for (int j = i; j > start; j--) {
			if ((number[new_start]) <= (number[j])) {
				new_start = j;
			}
		}
		answer[idx] = number[new_start];
		idx++;
		start = new_start;
	}
	answer[idx] = NULL;
	printf("%s %d\n",answer,number_len-k);
	return answer;
}

int main() {
	char nums[500] = "12612151515615155612131255125125125";
	for (int i = 0; i < strlen(nums); i++) {
		solution(nums, i);
	}
	return 0;
}