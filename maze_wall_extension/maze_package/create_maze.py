'''
Created on 2022/12/05

@author: User105
'''
from maze_package.range_check import maze_size_check
from test.test_buffer import numpy_array
import numpy as np

while True:
    height = int(input("生成する迷路の高さを入力してください。"))
    if maze_size_check(height):
        break

while True:
    width = int(input("生成する迷路の幅を入力してください。"))
    if maze_size_check(width):
        break
    
    
maze = np.array([[]])
for i in range(1, width - 2):
    maze[0][i] = "■"
    maze[]

