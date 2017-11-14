class mainClass():  
  inputTrainData = [[10.0,30.0],[11.0,29.0],[9.0,31.0],[30.0,11.0],[32.0,11.0],[29.0,9.0]]
  finalSlope = 1
  def __init__(self, x, y):
    self.x=x
    self.y=y   
  def func1(self):
    print(self.inputTrainData[1][0])
  def refine(self):
    a=(1.0)
    error=0
    currentSlope=0
    for i in range (0,5):
      error=(self.inputTrainData[i][1]/self.inputTrainData[i][0])-a
      a+=(error)/2
    self.finalSlope = a
  def solve(self):
    print(self.finalSlope)
    if ((self.y/self.x)>self.finalSlope):
      print("Group 1")
    else:
      print("Group 2")
if __name__ == "__main__":
  thing = mainClass(28,12)  
  thing.refine() 
  thing.solve()