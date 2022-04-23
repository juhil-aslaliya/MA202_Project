from turtle import *
from bezier import bezier_bernstein
from util import draw, transform
points = [[[25, 460], [35, 457], [60, 455], [60, 425]],
          [[60, 425], [60, 400], [25, 342], [25, 280]],
          [[25, 280], [25, 185], [80, 90], [195, 90]],
          [[195, 90], [290, 90], [335, 155], [390, 255]],
          [[390, 255], [475, 405], [510, 425], [565, 425]],
          [[565, 425], [620, 425], [675, 380], [675, 300]],
          [[675, 300], [675, 155], [545, 100], [500, 85]],
          [[500, 85], [710, 115]],
          [[710, 115], [700, 115], [675, 125], [675, 145]],
          [[675, 145], [675, 180], [710, 230], [710, 310]],
          [[710, 310], [710, 460], [615, 530], [530, 530]],
          [[530, 530], [320, 530], [300, 180], [160, 180]],
          [[160, 180], [95, 180], [65, 235], [65, 285]],
          [[65, 285], [65, 400], [155, 465], [235, 480]],
          [[235, 480], [25, 460]]]
penup()
bgcolor(0, 0, 0)
for i in points:
    transform(i, 355, 265, 1, [[0, 1], [-1, 0]])
    draw(i, 1, (1, 0, 0), 1, 6)
    lst = bezier_bernstein(i)
    penup()
    goto(lst[0][0], lst[0][1])
    pendown()
    draw(lst, 3, (0, 0, 1))
done()