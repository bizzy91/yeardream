#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:10:58 2021

@author: bizzy
"""
'''
재귀를 이용해서 병합 정렬을 구현할 수 있습니다. 
먼저 배열을 더 이상 나눌 수 없을 때 까지 (원소가 하나만 남을 때까지) 최대한 분할 후에, 
다시 병합하면서 점점 큰 배열을 만들어 나가면 됩니다. 
따라서 이 재귀 알고리즘의 기저 조건은 입력 배열의 크기가 2보다 작을 때이며, 
이 조건에 해당할 때는 배열을 그대로 반환하면 됩니다.

파이선의 리스트 slice notation(arr[start:end])을 사용하면 다음과 같이 간결한 코드를 작성할 수 있습니다. 
하지만, 리스트 slice를 할 때 배열의 복제가 일어나므로 메모리 사용 효율은 좋지 않습니다.

# 입력 예시
1 5 6 2 3 8 4 9 7 10

# 출력 예시
1 2 3 4 5 6 7 8 9 10

'''
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

'''
# In-place
# 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량을 대폭 줄일 수 있습니다.
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))
'''


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(*merge_sort(data))

if __name__ == "__main__":
    main()
