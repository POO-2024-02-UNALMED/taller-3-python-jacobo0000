class TV:
  numTV = 0
  def __init__(self, marca, estado):
    self.marca = marca
    self.estado = estado
    self.canal = 1
    self.precio = 500
    self.volumen = 1
    self.control = 0
    TV.numTV += 1

  def canalUp(self):
    if self.estado == True & self.canal < 120:
      self.canal += 1

  def canalDown(self):
    if self.estado == True & self.canal > 1:
      self.canal -= 1

  def volumenUp(self):
    if self.estado == True & self.volumen < 7:
      self.volumen += 1

  def volumenDown(self):
    if self.estado == True & self.volumen > 1:
      self.volumen -= 1

  def turnOn(self):
    self.estado = True

  def turnOff(self):
    self.estado = False

  def setCanal(self, canalNuevo):
    if self.estado == 1 & canalNuevo >= 1 & canalNuevo <= 120:
      self.canal = canalNuevo

  def setPrecio (self, precioNuevo):
    self.precio = precioNuevo

  def setVolumen (self, volumenNuevo):
    if self.estado == 1 & volumenNuevo >= 0 & volumenNuevo <= 7:
      self.volumen = volumenNuevo

  def setMarca (self, marcaNueva):
    self.marca = marcaNueva

  def setControl (self, controlNuevo):
    self.control = controlNuevo

  def getCanal (self):
    return self.canal

  def getPrecio (self):
    return self.precio

  def getVolumen (self):
    return self.volumen

  def getMarca (self):
    return self.marca

  def getControl(self):
    return self.control

  def getEstado (self):
    return self.estado
  
  @classmethod
  def setNumTV (self,numTVNuevo):
    TV.numTV = numTVNuevo

  @classmethod
  def getNumTV ():
    return TV.numTV