#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:36:55 2021

@author: bizzy
"""
'''
멱집합 구하기


집합 A에 대하여, A의 모든 부분집합을 원소로 가지는 집합을 A의 멱집합이라고 한다. 
예를 들어, 집합 A의 원소가 {1, 2, 3} 일 경우, A의 멱집합은 다음과 같이 8개의 원소를 갖는 집합이다.

{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}

집합 A의 원소는 1부터 n까지의 자연수로 구성된다. 
n이 주어질 때, A의 멱집합의 원소를 사전 순서대로 모두 출력하는 프로그램을 작성하시오. 
단, 공집합은 제외하고 출력한다.


# 입력 예시
3

#출력 예시

1
1 2
1 2 3
1 3
2
2 3
3
'''
def getPowerSet(n, k):
    '''
    1부터 n까지의 자연수인 원소가 있을 때, k를 가장 처음으로 선택하는 경우를 반환한다.
    getPowerSet(n, 1) = [ [1],  [1] + getPowerSet(n,2)[i] ]
                      = [ [1], [1,2],  [1,2] + getPowerSet(n,3)[i] ] 
                      = [ [1], [1,2],  [1,2] + [3],  [3] + getPowerSet(n,4)[i] ] 
                      = [ [1], [1,2],  [1,2,3],  [1,2,3] + getPowerSet(n,4)[i] ] 
                      = ... 
    getPowerSet(n, 2) = [ [2],  [2] + getPowerSet(n,3)[i] ]
    getPowerSet(n, 3) = [ [3],  [3] + getPowerSet(n,4)[i] ]
    ...
    getPowerSet(n, n-1) = [ [n-1],  [n-1] + getPowerSet(n,n)[i] ]
                        = [ [n-1],  [n-1, n] ]            
    getPowerSet(n, n) = [ [n] ]
    '''
    # getPowerSet(n, n) = [ [n] ]
    if n == k:
        return [[k]]
    # getPowerSet(n, n-1) = [ [n-1], [n-1] + getPowerSet(n,n-1)[i] ]
    result = [[k]]
    temp = []
    for i in range(k+1, n+1):
        temp += getPowerSet(n, i)
    for i in range(len(temp)):
        temp[i] = [k] + temp[i]
    return result + temp

def powerSet(n) :
    '''
    n개의 원소를 가지는 집합 A의 멱집합의 원소를 사전 순서대로 list로 반환하는 함수를 작성하시오.

    예를 들어, n = 3 일 경우 다음의 list를 반환한다.

    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''
    # 1부터 시작     -> getPowerSet(n, 1)
    # 2부터 시작     -> getPowerSet(n, 2) 
    # 3부터 시작     -> getPowerSet(n, 3)
    # ...
    # (n-1)부터 시작 -> getPowerSet(n, n-1)
    # [n]          -> getPowerSet(n, n)
    result = []
    for i in range(1, n+1):
        result += getPowerSet(n, i)

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    result = powerSet(n)
    
    for line in result :
        print(*line)

if __name__ == "__main__":
    main()
