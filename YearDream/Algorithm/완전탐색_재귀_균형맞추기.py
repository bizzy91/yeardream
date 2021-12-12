#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:29:36 2021

@author: bizzy
"""
'''
균형 맞추기


n개의 숫자가 주어진다. 
이제 이 숫자를 두 개의 그룹으로 나눌 것이다. 
예를 들어 5개의 숫자 [1, -3, 4, 5, -2] 가 주어진다면, 
이를 두 개의 그룹으로 나누는 경우는 여러가지가 있을 수 있다. 
가능한 경우로써 [1, -3], [4, 5, -2] 가 있을 수 있고, 
또 다른 경우로는 [1, 4, -2], [-3, 5] 가 있을 수 있다.

나눈 두 그룹을 A, B라고 할 때, 
(A의 원소의 합) - (B의 원소의 합) 의 절댓값을 최소화 하는 프로그램을 작성하시오. 
위의 예제에서는 A = [1, 4, -2], B = [-3, 5] 라고 하였을 때 
(A의 원소의 합) - (B의 원소의 합) 의 절댓값 = |3 - 2| = 1 이며, 
이보다 더 작은 값을 만드는 A, B는 존재하지 않는다. 이 경우 절댓값의 최솟값인 1을 출력하면 된다.


# 입력 예시
1 -3 4 5 -2

# 출력 예시
1
'''
import math
from 완전탐색_재귀_멱집합구하기 import powerSet

def makeEqual(data) :
    '''
    n개의 숫자를 두 그룹 A, B로 나눈다고 할 때,

    | (A의 원소의 합) - (B의 원소의 합) | 의 최솟값을 반환하는 함수를 작성하시오.
    '''
    
    combinations = powerSet(len(data))
    total = sum(data)
    result = math.inf
    
    for c in combinations:
        mySumA = 0
        mySumB = 0
        
        for i in c:
            mySumA += data[i-1]
            mySumB = total - mySumA
            
        result = min(result, abs(mySumA-mySumB))
        
    return result


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(makeEqual(data))

if __name__ == "__main__":
    main()
