def calcular_salario(horas_trabajadas, precio_hora, porcentaje_descuento):
    salario_bruto = calcular_salario_bruto(horas_trabajadas, precio_hora)
    descuento = calcular_descuento(salario_bruto, porcentaje_descuento)
    salario_neto = calcular_salario_neto(salario_bruto, descuento)
    return salario_neto

 
def calcular_salario_bruto(horas_trabajadas, precio_hora):
    salario_bruto = horas_trabajadas * precio_hora
    return salario_bruto

 
def calcular_descuento(salario_bruto, porcentaje_descuento):
    descuento = salario_bruto * (porcentaje_descuento / 100)
    return descuento

 
def calcular_salario_neto(salario_bruto, descuento):
    salario_neto = salario_bruto - descuento
    return salario_neto
   
horas_trabajadas = int(input("numero de horas trabajadas"))
precio_hora = int(input("precio por hora"))
porcentaje_descuento = int(input("porcentaje de descuento"))
salario_neto = calcular_salario(horas_trabajadas, precio_hora, porcentaje_descuento)
 
caso=1
while caso!=0:
   
    print("1.Calcular salario \n 2.Salario bruto \n 3.Calcular descuento \n 4.Calcular salario neto \n 0.Salir")
    caso=int(input("introduce un caso"))
    match caso:
        case 1:
             print(calcular_salario(horas_trabajadas, precio_hora, porcentaje_descuento))
        case 2:
             print(calcular_salario_bruto(horas_trabajadas,precio_hora))
        case 3:
             print(calcular_descuento(salario_bruto,porcentaje_descuento))
        case 4:
             print(calcular_salario_neto(salario_bruto,descuento))