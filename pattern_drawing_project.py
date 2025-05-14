print("Welcome to my pattern drawing project!\n\nPlease choose a shape you want to draw.")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Pyramid")
print("6. Reverse Pyramid")
print("7. Rectangle with Hollow Center")
print("8. Cancel Program")
rows, size = 0, 0

while True:
    pattern_type = int(input("Insert the number of the shape you liked:"))
    if pattern_type in [1, 3, 4, 5, 6]:
        rows = int(input("Please say how many rows would you like this shape to have:"))
    elif pattern_type in [2]:
        size = int(input("What size would you like this shape to be:"))
    elif pattern_type in [7]:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
    elif pattern_type == 8:
        print('Thank you for trying out my program!')
        break
#asdas

    if pattern_type == 1:
        for i in range(1, rows + 1):
            print("*" * i)
            pass

    elif pattern_type == 2:
        for i in range(size):
            if i == 0:
                for n in range(size):
                    print("*", end=" ")
                print()
            elif i == size - 1:
                for n in range(size):
                    print("*", end=" ")

            else:
                for m in range(size):
                    if m == 0:
                        print("*", end=" ")
                    elif m > 0 and m != size - 1:
                        print(" ", end=" ")
                    elif m == size - 1:
                        print("*")

    elif pattern_type == 3:
        for i in range(rows - 1, -1, -1):
            print(" " * i, end="")

            print("*" * (rows - i), end="")
            print("*" * ((rows - i) - 1))
        for i in range(rows - 1, -1, -1):
            print(" " * (rows - i), end="")

            print("*" * i, end="")
            print("*" * (i - 1))

    elif pattern_type == 4:
        for i in range(rows, 0, -1):
            print('*' * i)

    elif pattern_type == 5:
        for i in range(1, rows + 1, 2):
            print(' ' * ((rows - i) // 2), end='')
            print('*' * i)

    elif pattern_type == 6:
        for i in range(rows, 0, -2):
            print(' ' * ((rows - i) // 2), end='')
            print('*' * i)

    elif pattern_type == 7:
        for h in range(0, height):
            if h == 0 or h == height - 1:
                print('*' * width)
            else:
                for w in range(0, width):
                    if w == 0:
                        print('*', end='')
                    elif w == width - 1:
                        print('*')
                    else:
                        print(' ', end='')


