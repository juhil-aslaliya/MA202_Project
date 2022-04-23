from turtle import *
from bspline import bspline1
from util import draw
points = [[0, 100], [50, 200], [100, 100], [200, 50], [100, 0], [100, 0], [200, -50], [100, -100], [50, -200],
          [0, -100], [0, -100], [-50, -200], [-100, -
                                              100], [-200, -50], [-100, 0], [-100, 0], [-200, 50],
          [-100, 100], [-50, 200], [0, 100], [0, 100], [25,
                                                        25], [100, 0], [100, 0], [25, -25], [0, -100],
          [0, -100], [-25, -25], [-100, 0], [-100, 0], [-25, 25], [0, 100], [0, 100]]
bgcolor(0, 0, 0)
draw(points, 1, (1, 0, 0), 1, 6)
lst = bspline1(points)
penup()
goto(points[0])
pendown()
draw(lst, 3, (0, 0, 1))
done()
