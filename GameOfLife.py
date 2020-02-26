from Box import Box

box = 1

def firstStep():
    #return row and col

    global box
    row = eval(input("Enter the row of the grid:  "))
    col = eval(input("Enter the col of the grid:  "))

    box = Box(row, col)


def set_alive():
    #return box

    alive_cells = eval(input("How many alive cells you want to insert:  "))

    for i in range(alive_cells):

        row = eval(input("Row: "))
        col = eval(input("Col: "))

        box.grid[row - 1][col - 1] = 1

    return box

def main():
    firstStep()
    set_alive()
    print(box.box_printer())


main()
