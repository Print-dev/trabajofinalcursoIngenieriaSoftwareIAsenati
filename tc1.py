class Trabajador():
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def mostrarSueldo(self):
        if(self.categoria == "A"):
            return 3000
        if(self.categoria == "B"):
            return 2500
        if(self.categoria == "C"):
            return 2000
    
class Boleta():
    def __init__(self, horasExtras, tardanzasMin, categoria):
        self.horasExtras = horasExtras
        self.tardanzasMin = tardanzasMin
        self.categoria = categoria 

    def descuentoTardanzas(self):
        sba = 3000
        sbb = 2500
        sbc = 2000

        if(self.categoria == "A"):
            dsctTardanzas = (sba / 240)/60 * self.tardanzasMin
            return dsctTardanzas
        if(self.categoria == "B"):
            dsctTardanzas = (sbb / 240)/60 * self.tardanzasMin
            return dsctTardanzas
        if(self.categoria == "C"):
            dsctTardanzas = (sbc / 240)/60 * self.tardanzasMin
            return dsctTardanzas

    def pagoHorasExtras(self):
        sba = 3000
        sbb = 2500
        sbc = 2000

        if (self.categoria == "A"):
            ph = sba / 240
        elif (self.categoria == "B"):
            ph = sbb / 240
        elif (self.categoria == "C"):
            ph = sbc / 240
        
        if (self.categoria == "A"):
            phx = ph * self.horasExtras
            return phx
        elif (self.categoria == "B"):
            phx = ph * self.horasExtras
            return phx
        elif (self.categoria == "C"):
            phx = ph * self.horasExtras
            return phx
    
    def sueldoNeto(self):
        sba = 3000
        sbb = 2500
        sbc = 2000

        if (self.categoria == "A"):
            dsct = (sba / 240)/60 * self.tardanzasMin
            ph = sba / 240
            phx = ph * self.horasExtras
            neto = (sba - dsct) + phx
            return neto
        if (self.categoria == "B"):
            dsct = (sbb / 240)/60 * self.tardanzasMin
            ph = sbb / 240
            phx = ph * self.horasExtras
            neto = (sbb - dsct) + phx
            return neto
        if (self.categoria == "C"):
            dsct = (sbc / 240)/60 * self.tardanzasMin
            ph = sbc / 240
            phx = ph * self.horasExtras
            neto = (sbc - dsct) + phx
            return neto

print("**** DATOS DE ENTRADA ********")

nombre = input("NOMBRE: ")
categoria = input("CATEGORIA: ")
hextras = int(input("HORAS EXTRAS: "))
tardanzas = int(input("TARDANZAS (MINUTOS): "))

t1 = Trabajador(nombre, categoria)
b1 = Boleta(hextras, tardanzas, categoria)

print("**** BOLETA DE PAGO *******")
print("NOMBRE: ",t1.nombre)
print("CATEGORIA: ",t1.categoria)
print("SUELDO BASICO: ", t1.mostrarSueldo())
print("DESCUENTO TARDANZAS: ", b1.descuentoTardanzas())
print("PAGO POR HORAS EXTRAS: ", b1.pagoHorasExtras())
print("SUELDO NETO: ", b1.sueldoNeto())
        
        
            
            