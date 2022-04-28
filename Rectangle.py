class Rectangle: 
  def __init__ (self, x=0,y=0,h=0,w=0 ):
    if x < 0:
      self.x = 0
    else:
      self.x = x
    if y < 0:
      self.y = 0
    else:
      self.y = y
    if h < 0 :
      self.height = 0
    else:
      self.height=h
    if w < 0:
      self.width = 0
    else:
      self.width=w
    ''' makes the x,y,h,w, if statesments for values less than 0, arg= self,x,y,h,w, returns nothing'''
  def __str__ (self):
    return str("(x: "+ str(self.x)+ ", y: " + str(self.y) + ") width: "+ str(self.width)+ ", height: " + str(self.height))

''' returns the statement to give the values, arg self, gives the string'''