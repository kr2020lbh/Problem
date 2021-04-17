#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// �Ķ���ͷ� �־����� ���ڿ��� const�� �־����ϴ�. �����Ϸ��� ���ڿ��� �����ؼ� ����ϼ���.
char* solution(const char* number, int k) {
	// return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
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