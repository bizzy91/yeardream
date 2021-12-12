#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:23:39 2021

@author: bizzy
"""
'''
N-Queen


n x n 의 체스 판에 n개의 Queen을 놓으려 합니다. 
이 때, 다음의 규칙을 반드시 따라야 합니다.

1. 같은 행에 2개 이상의 Queen이 존재해서는 안됩니다.
2. 같은 열에 2개 이상의 Queen이 존재해서는 안됩니다.
3. 하나의 대각선에 2개 이상의 Queen이 존재해서는 안됩니다. 
이는 ‘\‘ 방향의 대각선과 ‘/‘ 방향의 대각선 모두에 대하여 해당되는 조건입니다.

n이 주어질 때, n개의 Queen을 배치할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.


# 입력 예시 1
4

# 출력 예시 1
2

# 입력 예시 2
5

# 출력 예시 2
10
'''
import sys
import itertools
sys.setrecursionlimit(100000)

# 각 행과 열에 하나씩만 존재하는 퀸들이
# 대각선으로 겹치는지 아닌지 알아보는 함수.
def isPossible(locations, n) :
    # 우하향 대각선
    diagnalCheck1 = [0 for i in range(n+n)]
    # 우상향 대각선
    diagnalCheck2 = [0 for i in range(n+n)]
    
    
    for i in range(n) :
        diagnalCheck1[locations[i]-i + n] += 1
        diagnalCheck2[locations[i]+i - n] += 1
    
    for i in range(n+n) :
        if diagnalCheck1[i] >= 2 or diagnalCheck2[i] >= 2 :
            return False

    return True

def nQueen(n) :
    '''
    n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
    '''
    
    # 0번 퀸부터 n-1번까지 만들어준 리스트
    myList = [i for i in range(n)]
    
    # 각 퀸들을 배치할 각각의 경우의 수
    perm = list(itertools.permutations(myList))
    
    result = 0
    for p in perm :
        if isPossible(p, n) == True :
            result += 1
    
    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(nQueen(n))

if __name__ == "__main__":
    main()
