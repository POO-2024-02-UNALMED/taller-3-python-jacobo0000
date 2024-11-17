class Control:
  def __init__(self):
    self.tv = 0

  def enlazar(self, tv):
    self.tv = tv
    tv.control = self
  
  def turnOn(self):
    self.tv.turnOn()

  def turnOff(self):
    self.tv.turnOff()

  def canalUp(self):
    self.tv.canalUp()

  def canalDown(self):
    self.tv.canalDown()

  def volumenUp(self):
    self.tv.volumenUp()

  def volumenDown(self):
    self.tv.volumenDown()

  def setCanal(self, canalNuevo):
    self.tv.setCanal(canalNuevo)
  
  def setVolumen(self, volumenNuevo):
    self.tv.setVolumen(volumenNuevo)

  def setTv(self,tvNuevo):
    self.tv = tvNuevo

  def getTv(self):
    return self.tv