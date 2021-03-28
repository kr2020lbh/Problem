#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

	char* solution(int n) {

		char* answer = (char*)malloc(sizeof(char) * (n * 3) + 1);
		strcpy(answer, "");
		int i = 0;
		for (i; i < n; i++) {
			if (i % 2 == 0)  strcat(answer, "¼ö");
			else strcat(answer, "¹Ú");
		}
		return answer;
	}
int main() {
    solution(4);
    return 0;
}