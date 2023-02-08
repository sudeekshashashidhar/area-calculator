def area_calculator():
  shape = input("Enter the shape that you want to calculate the area of(Use only small letters!!): ")
  area = 0
  pie = 3.14

  if shape == "square":
    side = int(input("Enter the value of the sides of your square: "))
    area = area + (side ** 2)
  elif shape == "rectangle":
    length = int(input("Enter the value of the length of your rectangle: "))
    width = int(input("Enter the value of the width of your rectangle: "))
    area = area + (length * width)
  elif shape == "triangle":
    base = int(input("Enter the value of base for your triangle: "))
    height = int(input("Enter the value of height for your triangle: "))
    area = area + (0.5 * base * height)
  elif shape == "circle":
    radius = int(input("Enter the radius of your circle: "))
    area = area +(2 * pie * radius)
  else:
    print("That's not a valid shape. Can't find the area.")
  print("%.2f" % area)


area_calculator()
    
  
  