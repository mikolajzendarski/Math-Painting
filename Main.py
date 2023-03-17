from Canvas import Canvas
from Shapes import Square, Rectangle

# Get canvas width and height from user"
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? (rectangle or square) Enter quit to quit. ")
    # ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should rectangle have: "))
        green = int(input("How much green should rectangle have: "))
        blue = int(input("How much blue should rectangle have: "))

        # Create rectangle
        rec = Rectangle(rec_x, rec_y, rec_width, rec_height, (red, green, blue))
        rec.draw(canvas)
    # ask for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side length of the square: "))
        red = int(input("How much red should square have: "))
        green = int(input("How much green should square have: "))
        blue = int(input("How much blue should square have: "))
        # Create square
        sqr = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        sqr.draw(canvas)

    # Breake the loop if user entered 'quit'
    if shape_type == 'quit':
        break

    canvas.make('canvas.png')