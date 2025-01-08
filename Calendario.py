############################################################################
#                                                                          #
#       ESTE CÓDIGO NO FUNCIONA BIEN Y RESCRIBE LAS CLASES DE INGLÉS       #
#                                                                          #
############################################################################
#pendiente de arreglar
#puede ser usado para cualquier rutina 
#ejecutando una sola vez funciona, a la segunda hay que borrar excedente


import pandas as pd

df=pd.read_csv('Calendario.csv')

mes=1
dia=10
grandes=[1,3,5,7,8,10,12]
pequeños=[4,6,9,11]

while mes <=6:
    if mes ==2:
        tope=28
    elif mes in grandes:
        tope=31
    else:
        tope=30
    while dia<=tope:
        f=f'{dia}/{mes}/2025'
        Clase={'Asunto':'Inglés Eva','Fecha de comienzo':f,'Comienzo':'10:00','Fecha de finalización':f,
               'Finalización':'12:00','Todo el dí­a':'FALSO','Reminder on/off':'FALSO','Reminder Date':f,
               'Reminder Time':'9:30','Meeting Organizer':'Eva','Required Attendees':'',
               'Optional Attendees':'','Recursos de la reuniÃƒÂ³n':'','Billing Information':'',
               'Categories':'','Description':'','Location':'','Mileage':'','Priority':'','Private':'Falso',
               'Sensitivity':'Normal','Show time as':2}        
        if Clase not in df.to_dict('records'): 
            Clase=pd.DataFrame([Clase])
            df=pd.concat([df,Clase], ignore_index=True)
        dia+=7
    dia=dia-tope
    mes +=1
print(df)
df.to_csv('Calendario.csv',index=False)