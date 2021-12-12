#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:06:35 2021

@author: bizzy
"""
'''
기울기가 가장 큰 두 점 찾기


2차원 평면에 n개의 점이 있다. 
이 점들 중에서 두 점을 선택했을 때, 
그 기울기 절댓값의 집합 중 최댓값을 출력하는 프로그램을 작성하시오. 
단, 모든 점의 x좌표는 다르다고 가정한다. 
또한, 두 점 (x1, y1), (x2, y2)의 기울기는 (y2 - y1) / (x2 - x1) 으로 정의된다.

예를 들어, 4개의 점이 각각 (0, 3), (1, 1), (2, 2), (4, 1) 에 위치해 있다고 하자. 
이 경우의 최댓값은 (0, 3), (1, 1) 의 두 점의 기울기의 절대값인 2가 된다.

입력으로는 첫줄에 점의 개수가, 그 다음줄부터는 점의 xx좌표와 yy좌표가 입력됩니다.


# 입력 예시
4
0 3
1 1
2 2
4 1

# 출력 예시
2.000
이 경우 기울기 절댓값의 최댓값인 2를 출력한다.
'''
from itertools import combinations

def maxSlope(points) :
    '''
    n개의 점들 중에서 2개의 점을 선택했을 때, 얻을 수 있는 기울기의 절댓값 중에서 가장 큰 값을 반환하는 함수를 작성하세요.
    **주의** : 소숫점 넷째자리에서 반올림하는 것은 고려할 필요가 없습니다. 이는 main()에서 출력을 할 때에 처리가 되므로, 기울기의 최댓값을 구하는 것에 집중해 주시길 바랍니다.
    '''
    gradients = []
    for p in combinations(points, 2):
        p1_x, p1_y = p[0][0], p[0][1]
        p2_x, p2_y = p[1][0], p[1][1]
        gradients.append(abs((p2_y - p1_y) / (p2_x - p1_x)))
    return max(gradients)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    points = []

    for i in range(n) :
        line = [int(x) for x in input().split()]
        points.append( (line[0], line[1]) )

    print("%.3lf" % maxSlope(points))

if __name__ == "__main__":
    main()
