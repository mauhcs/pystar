class ARColor:
  def __init__(self, name, metal=0, rough=0.5):
    self.name  = name
    self.metal = metal
    self.rough = rough

  def __str__(self):
    return f"ARColor('{self.name}', {self.metal}, {self.rough})"

  def __repr__(self):
    return self.__str__()

class Material:
  def __init__(self, metal, rough):
    self.metal = metal
    self.rough = rough
    
  def color(self, name):
    return ARColor(name, self.metal, self.rough)

  def __str__(self):
    return f"Material({self.metal}, {self.rough})"
  
  def __repr__(self):
    return self.__str__()

class Materials:
  Metal = Material(1,0)
  Candy = Material(0.1,0.5)