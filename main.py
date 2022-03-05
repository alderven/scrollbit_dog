import time
import scrollbit
x = -12
while True:
    for array in [[(3, 6), (4, 5), (5, 4), (4, 3), (3, 2), (6, 4), (7, 4), (8, 4), (9, 4), (8, 5), (7, 6), (10, 3), (10, 2), (11, 2), (11, 3)],
                  [(5, 6), (5, 5), (5, 4), (4, 3), (3, 2), (6, 4), (7, 4), (8, 4), (9, 4), (9, 5), (9, 6), (10, 3), (10, 2), (11, 2), (11, 3)]]:            
        scrollbit.clear()
        x += 1
        for el in array:
            try:
                scrollbit.set_pixel(x+el[0], el[1], 10)
            except:
                pass
        scrollbit.show()
        time.sleep(0.1)
        if x > 15:
            x = -12
