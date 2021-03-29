#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
int solution(int n) {
	int visited[3000] = { 0, };
	int answer = 0;
	for (int i = 1; i < sqrt(n) + 1; i++) {
		if (n % i == 0 && !visited[i]) {
			if (n / i == i) {
				visited[i] = 1;
				answer += i;	
			}
			else {
				visited[i] = 1;
				visited[n / i] = 1;
				answer += i + n / i;
			}
		}
	}
	return answer;
}

int main() {
	solution(12);
	
}