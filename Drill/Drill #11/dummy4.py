from pico2d import *
a = 1000
a = min(a, 800)  # 최대값을 800으로 제한
print(a)
a = -1
a = max(a, 0)  # 최소값을 0으로 제한
print(a)
a = -1
a = clamp(0, a, 800)  # 최솟값을 0, 최댓값을 800으로 제한
print(a)
a = 1000
a = clamp(0, a, 800)
print(a)
