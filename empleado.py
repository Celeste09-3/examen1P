from abc import ABC, abstractmethod

class EmpleadoC(ABC):
    @abstractmethod
    def __init__(self,RFC,apellidos,nombres):
        self.RFC=RFC
        self.apellidos=apellidos
        self.nombres=nombres
    def informacion_emp(self):
       pass
    
class EmpleadoVendedorC(EmpleadoC):
    def __init__(self,monto_vendido,tasa_comision):
        self.monto_vendido=monto_vendido
        self.tasa_comision=tasa_comision
        
    def ingresos(self):
        return self.monto_vendido*self.tasa_comision
        
    def bonificacion(self):
        if self.monto_vendido<1000:
            print("No hay bonificacion")
        elif self.monto_vendido > 1000 and self.monto_vendido<=5000:
            print("Bono del 5%")
        elif self.monto_vendido > 5000:
            print("Bono del 10%" )
        else:
            print("Error")
    
    def descuentos(self): 
        pass
    def sueldo_neto(self):
        return 
class EmpleadoPermanente(EmpleadoC):
    def __init__(self,sueldo_base, num_ss):
        self.sueldo_base=sueldo_base
        self,num_ss=num_ss
    
    def sueldo_b(self):
        pass
    def descuento_ss(self):
        pass
    def sueldo_neto(self):
        pass
    