# bounce.py
#
# Exercise 1.5

height = 100    # Initial height of the drop in meters
bounce = 0.6    # Return height (3/5 th's of the drop height)

for i in range(10):
    height = height * bounce
    print(round(height, 4))

