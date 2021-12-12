#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:31:01 2021

@author: bizzy
"""
'''
연속 부분 최대합(완전탐색)

n개의 숫자가 주어질 때, 연속 부분을 선택하여 그 합을 최대화 하는 프로그램을 작성하시오. 
예를 들어, 다음과 같이 8개의 숫자가 있다고 하자.

1 2 -4 5 3 -2 9 -10

이 때, 연속 부분이란 연속하여 숫자를 선택하는 것을 말한다. 
가능한 연속 부분으로써 [1, 2, -4], [5, 3, -2, 9], [9, -10] 등이 있을 수 있다. 
이 연속 부분들 중에서 가장 합이 큰 연속 부분은 [5, 3, -2, 9] 이며, 
이보다 더 합을 크게 할 수는 없다. 
따라서 연속 부분 최대합은 5+3+(-2)+9 = 15 이다.

# 입력 예시 
1 2 -4 5 3 -2 9 -10

# 출력 예시
15
'''
import math


def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    result = -math.inf
    temp = 0
    # start <- 0 ~ len(data)
    for start in range(0, len(data)):
        # end <- start ~ len(data)
        for end in range(start, len(data)):
            temp = 0
            # start ~ end 구간을 완전히 탐색
            # 모든 데이터를 더하여 temp 와 result를 비교하여 최대값 갱신
            for i in range(start, end+1):
                temp += data[i]
            result = max(result, temp)
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
