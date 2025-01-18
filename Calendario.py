import pandas as pd

df=pd.read_csv('Calendario.csv')

mes=1; dia=10 #fecha de inicio

grandes=[1,3,5,7,8,10,12]; pequeños=[4,6,9,11] #nº días de cada mes

while mes <=6:
    if mes ==2:
        tope=28
    elif mes in grandes:
        tope=31
    else:
        tope=30
    while dia<=tope:
        f=f'{dia}/{mes}/2025'
        
        #Crear la fila
        Clase={'Asunto':'Inglés Eva',
               'Fecha de comienzo':f,
               'Comienzo':'10:00',
               'Fecha de finalización':f,
               'Finalización':'12:00',
               'Todo el dí­a':'FALSO',
               'Reminder on/off':'FALSO',
               'Reminder Date':f,
               'Reminder Time':'9:30',
               'Meeting Organizer':'Eva',
               'Required Attendees':'',
               'Optional Attendees':'',
               'Recursos de la reuniÃƒÂ³n':'',
               'Billing Information':'',
               'Categories':'',
               'Description':'',
               'Location':'',
               'Mileage':'',
               'Priority':'',
               'Private':'Falso',
               'Sensitivity':'Normal',
               'Show time as':2}
        
        #Comprobar que la fila no existe en el calendario e introducirla
        if df[(df['Asunto'] == 'Inglés Eva') & (df['Fecha de comienzo'] == f) & (df['Comienzo']=='10:00')].empty:
            Clase=pd.DataFrame([Clase])
            df=pd.concat([df,Clase], ignore_index=True)
        
        #Continuar bucle
        dia+=7
    dia=dia-tope
    mes +=1

#Eliminar festivos
festivos = ['1/1/2025', '6/1/2025', '17/4/2025', '18/4/2025', '1/5/2025', '15/8/2025', 
            '8/9/2025', '13/10/2025', '1/11/2025', '6/12/2025', '8/12/2025', '25/12/2025']

#Filtrar las filas que no estén en festivos
df = df[~df['Fecha de comienzo'].isin(festivos)]


#print(df)
df.to_csv('Calendario.csv',index=False)


 
