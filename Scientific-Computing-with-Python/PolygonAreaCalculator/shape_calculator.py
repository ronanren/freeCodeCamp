class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    result = ""
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      for i in range(1, self.height+1):
        result += "*" * self.width + "\n"
    return result

  def get_amount_inside(self, obj):
    nbrwidth = self.width / obj.width
    nbrheight = self.height / obj.height
    return int(nbrwidth) * int(nbrheight)

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side
    Rectangle.__init__(self, side, side)
  
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.width = height
    self.height = height
  
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"