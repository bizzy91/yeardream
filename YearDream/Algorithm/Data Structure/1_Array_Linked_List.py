#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:20:40 2021

@author: bizzy
"""

"""
구슬 넣기 (배열)
Elice의 토끼는 암기력을 높이기 위해 구슬 넣기 놀이를 고안했습니다.

토끼는 n개의 구슬이 있으며, 각 구슬은 1부터 n까지의 번호를 하나씩 갖고 있습니다. 
또한, 토끼는 양 쪽이 뚫려있고 투명하지 않은 관을 갖고 있습니다.

토끼는 n개의 구슬을 이 파이프에 무작위로 넣은 후에, 
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 암기함으로써 암기력을 높이려고 합니다.

토끼는 파이프의 왼쪽에, 혹은 오른쪽에 구슬을 넣을 수 있습니다. 
예를 들어, 파이프의 왼쪽으로 숫자 1의 구슬을 넣고, 파이프의 오른쪽으로 숫자 3의 구슬을 넣고, 
마지막으로 파이프의 왼쪽으로 숫자 2의 구슬을 넣게 되면, 최종적으로 구슬의 배치는 2 1 3 이 됩니다.

토끼가 n개의 구슬을 파이프에 넣는 행위가 입력으로 주어질 때, 
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력하는 프로그램을 작성하세요.

(단, 파이프의 길이는 n개의 구슬을 모두 담기에 충분히 길다고 가정합니다.)


지시사항
입력
입력의 첫 번째 줄에는 구슬의 개수 n이 주어집니다. (100 <= n <= 200000)

두 번째 줄부터는 토끼가 구슬을 넣는 행위가 주어집니다.

각 줄은 두 개의 정수 a, b로 이루어지며, 이 뜻은 구슬 a를 왼쪽 혹은 오른쪽으로 넣는다는 의미입니다. 
(1 ≤ a ≤ 1000000000)
(b가 0이면 왼쪽, b가 1이면 오른쪽이며 그 외의 입력은 주어지지 않는다)

출력
최종적으로 구슬이 파이프 속에서 어떻게 배치되어 있는지를 출력한다.

입력 예시
3
1 0
2 1
3 0

출력 예시
3 1 2
"""

# Array (List)
class ListPipe:
    def __init__(self) :
        # 리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        self.myPipe = []

    # 파이프의 왼쪽으로 구슬 n을 삽입합니다
    def addLeft(self, n) :
        self.myPipe.insert(0, n)

    # 파이프의 오른쪽으로 구슬 n을 삽입합니다.
    def addRight(self, n) :
        self.myPipe.append(n)

    # 파이프의 배치를 list로 반환합니다.
    def getBeads(self) :
        return self.myPipe

# Linked List
class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

class LinkedListPipe:
    def __init__(self) :
        # 리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        self.start = None
        self.end = None

    # 파이프의 왼쪽으로 구슬 n을 삽입합니다.
    def addLeft(self, n) :
        if self.start == None and self.end == None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, self.start)
            self.start = element

    # 파이프의 오른쪽으로 구슬 n을 삽입합니다.
    def addRight(self, n) :
        if self.start == None and self.end == None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, None)
            self.end.myNext = element
            self.end = element

    # 파이프의 배치를 list로 반환합니다.
    def getBeads(self) :
        result = []
        current = self.start
        while current != None:
            result.append(current.value)
            current = current.myNext
        
        return result
        

def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 
    1 0
    2 1
    3 0
    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''

    # myPipe = ListPipe()
    myPipe = LinkedListPipe()
    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)

    result = myPipe.getBeads()

    return result

n = int(input())

myList = []

for i in range(n) :
    myList.append([int(v) for v in input().split()])

print(*processBeads(myList))