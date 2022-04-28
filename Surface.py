import Rectangle

class Surface:
  def __init__ (self, filename, x,y,h,w):
    self.image= filename #pygame.image.load(file_name)
    self.rect= Rectangle.Rectangle(x,y,h,w)
  ''' 
makes the objectm, arg= self, filename, x,y,h,w, returns:none
'''
  def getRect(self):
    return  (self.rect)
    '''gets the rectangle, argu= self, returns self.rect'''