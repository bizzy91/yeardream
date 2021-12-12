#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:09:17 2021

@author: bizzy
"""
'''
거듭제곱 구하기


본 연습문제에서는 m^n 을 구하는 프로그램을 작성합니다.

입력으로는 m, nm,n이 차례대로 입력됩니다.

만약 getPower 함수의 반환 값이 1,000,000,007 보다 클 경우, 
반환 값을 1,000,000,007로 나눈 나머지 값을 반환하세요.

# 입력 예시
3 4

# 출력 예시
81
'''
LIMIT_NUMBER = 1000000007


def getPower(m, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = getPower(m, n // 2)
        return (temp*temp) % LIMIT_NUMBER        
    else:
        temp = getPower(m, (n - 1) // 2)
        return (temp*temp*m) % LIMIT_NUMBER

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    myList = [int(v) for v in input().split()]

    print(getPower(myList[0], myList[1]))

if __name__ == "__main__":
    main()
