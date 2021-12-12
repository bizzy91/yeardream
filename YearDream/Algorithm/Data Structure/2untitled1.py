#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:51:03 2021

@author: bizzy
"""

class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r
        '''
        # Root 노드
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None
        
            return True
        
        else:
            flag = False            
            if self.left != None:
                flag = self.left.addNode(i, l, r)
                
            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)
                
            return flag
'''
preorder, inorder, postorder 함수를 구현하세요.
'''

def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    result.append(tree.index)
    
    if tree.left != None:
        result += preorder(tree.left)
    if tree.right != None:
        result += preorder(tree.right)
        
    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    if tree.left != None:
        result += inorder(tree.left)

    result.append(tree.index)

    if tree.right != None:
        result += inorder(tree.right)

    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []

    if tree.left != None:
        result += postorder(tree.left)

    if tree.right != None:
        result += postorder(tree.right)

    result.append(tree.index)

    return result