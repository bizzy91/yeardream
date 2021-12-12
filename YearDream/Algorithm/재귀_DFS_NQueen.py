# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
sys.setrecursionlimit(100000)


def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    # 가로
    for col in range(n):
        # 주어진 행에 1개의 퀸을 놓는다.
        queen[row] = col
        for i in range(row):
            # 1. 같은 행에 2개 이상의 Queen이 존재해서는 안됩니다.
            if queen[i] == queen[row]:
                break
            # 3. 하나의 대각선에 2개 이상의 Queen이 존재해서는 안됩니다. 이는 ‘\‘ 방향의 대각선과 ‘/‘ 방향의 대각선 모두에 대하여 해당되는 조건입니다.
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def nQueen(n) :
    '''
    n개의 Queen을 배치하는 경우의 수를 반환하는 함수를 작성하세요.
    '''

    return dfs([0]*n, 0, n)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    print(nQueen(n))

if __name__ == "__main__":
    main()
