dia=input ("Ingrese el dia: ")
dia=dia.lower()
fecha=int(input ("Ingrese la fecha: "))
mes=int(input ("Ingrese el mes: "))
dias_semana=["lunes", "martes", "miercoles", "jueves", "viernes"]

if(dia) not in dias_semana:
    print("Error")

elif(fecha)<1 or fecha>31:
    print("Error")

elif(mes)<1 or mes>12:
    print("Error")

else:
    print(dia, ",", fecha, "/", mes)
    if dia in ["lunes", "martes", "miercoles"]:
            examenes=(input("Se tomaron examenes?(responda con si o no): "))
            examenes=examenes.lower()

            if (examenes=="si"):
                aprobados=int(input("Ingrese la cantidad de alumnos aprobados: "))
                desaprobados=int(input("Ingrese la cantidad de alumnos desaprobados: "))
                sumalumnos = (aprobados + desaprobados)
                porcentaje_aprobados = (aprobados/sumalumnos)*100
                print('El porcentaje de alumnos aprobados fue', porcentaje_aprobados, "%")
                
            elif(examenes=="no"):
                print("No se tomaron examenes en ese dia")

            else:
                print("Error")

    elif dia in ["jueves"]:
            porcentaje_asistencias=float(input("Ingrese el porcentaje de alumnos que asistieron: "))
            if porcentaje_asistencias>50:

                print("Asistio la mayoria")

            else:
                print("No asistio la mayoria")

    elif dia in ["viernes"] and (mes==1 or mes==7) and fecha == 1:
            cantidad_alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel_alumnos=float(input("Ingrese el arancel por alumno: "))
            total=cantidad_alumnos*arancel_alumnos
            print("Ingreso total: $", total)
            print("Comienza un nuevo ciclo")

    else:
            print("Error")
