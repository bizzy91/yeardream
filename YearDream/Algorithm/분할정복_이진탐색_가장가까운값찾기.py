#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:44:11 2021

@author: bizzy
"""
'''
가장 가까운 값 찾기


오름차순으로 정렬된 n개의 숫자가 주어지고, 정수 m이 주어질 때, 
n개의 숫자 중에서 m과 가장 가까운 숫자를 출력하는 프로그램을 작성하시오. 
만약 가장 가까운 숫자가 2개 이상이라면, 그 중 가장 작은 숫자를 출력한다.


# 입력 예시 1
1 4 6 7 10 14 16
8

# 출력 예시 1
7

# 입력 예시 2
1 4 6 7 10 14 16
12

# 출력 예시 2
10
'''

# m과 가장 가까운 두 값(하나는 크고 하나는 작음)을 반환
def getNearestInternal(data, m):
    if len(data) == 1:
        return (data[0], data[0])
    elif len(data) == 2:
        return (data[0], data[1])
    
    mid = len(data) // 2
    if data[mid] <= m:
        return getNearestInternal(data[mid:], m)
    else:
        return getNearestInternal(data[:mid+1], m)

def getNearest(data, m) :
    '''
    n개의 숫자가 list로 주어지고, 숫자 m이 주어질 때, 
    n개의 숫자 중에서 m과 가장 가까운 숫자를 반환하는 함수를 작성하세요.
    
    1. data 안에 m이 있는 경우 -> (m, m) 반환
    2. data 안에 m이 없는 경우 -> (value[0], value[1]) 반환
        value[0] : m 이하이면서 가장 가까운 값
        value[1] : m 이상이면서 가장 가까운 값
    '''
    value = getNearestInternal(data, m)
    if m - value[0] <= value[1] - m:
        return value[0]
    else:
        return value[1]

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]
    m = int(input())

    print(getNearest(data, m))

if __name__ == "__main__":
    main()



