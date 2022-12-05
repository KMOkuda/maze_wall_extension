'''
Created on 2022/12/05

@author: User105
'''

def maze_size_check(value):
    if value >= 5 and value <= 41 and value % 2 == 1:
        return True
    else:
        print("5以上41の奇数の数字を入力してください")
        return False