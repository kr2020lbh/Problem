#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// skill_trees_len은 배열 skill_trees의 길이입니다.
int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
	int skill_len = strlen(skill);
	int answer = 0;
	int idx,flag;
	for (int i = 0; i < skill_trees_len; i++) {
		idx = 0;
		flag = 0;
		for (int j = 0; j < strlen(skill_trees[i]); j++) {
			if (flag) {
				break;
			}
			if (skill_trees[i][j] == skill[idx]) {
				idx++;
			}
			else {
				for (int k = idx+1; k < skill_len; k++) {
					if (skill[k] == skill_trees[i][j]) {
						flag = 1;
						break;
					}
				}
			}
		}
		if (!flag ) {
			answer++;
		}
	}
	return answer;
}