import numpy as np

robots = []
with open('input.txt') as f:
    for li in f.readlines():
        robot = {}
        p_str, v_str = li.removesuffix('\n').split(' ')
        robot['p'] = [int(n) for n in p_str.split('=')[-1].split(',')]
        robot['v'] = [int(n) for n in v_str.split('=')[-1].split(',')]
        robots.append(robot)

width, height = 101, 103
num_step = 100

tiles = np.zeros((height, width))
for robot in robots:
    robot_x = (robot['p'][0] + num_step * robot['v'][0]) % width
    robot_y = (robot['p'][1] + num_step * robot['v'][1]) % height
    tiles[robot_y, robot_x] += 1

tiles_ul = tiles[:int(height/2), :int(width/2)]
tiles_ur = tiles[:int(height/2), int(width/2)+1:]
tiles_dl = tiles[int(height/2)+1:, :int(width/2)]
tiles_dr = tiles[int(height/2)+1:, int(width/2)+1:]

s = tiles_ul.sum() * tiles_ur.sum() * tiles_dl.sum() * tiles_dr.sum()
