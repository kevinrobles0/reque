#Librerias a importar
from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup
import re
import calendar
import goslate
import os
from socket import *

def determinarFestividades(anno, pais) :
    #validacion de tipo de dato
    if isinstance(anno,int) and isinstance(pais,str):
        pais = pais.lower()#Pais a minusculas
        #Para el caso de los paises con mas de dos palabras
        if(len(pais.split())>1):
            pais = pais.replace(" ","-")
            #construir URL a consultar
            my_url = "http://www.cuandoenelmundo.com/calendario/"+pais+"/"+str(anno)
            try:
                uClient = uReq(my_url)#conección a url    
                page_html = uClient.read()#obtener datos de url
                uClient.close()#cerrar coneccion

                page_soup = soup(page_html,"html.parser")#parsear datos de página
                hdays = page_soup.find('div',{'class':"hdays"})#buscar seccion de días festivos
                table = hdays.find_all('table',{'class':"hdays"})#buscar tabla de días destivos
                #por cada tabla encontrada
                for element in table:  
                    dia = element.find_all('td')#fechas encontradas
                    dia = re.sub('<[^>]*>', '', str(dia))#eliminar texto inncesario
                    dia = dia.replace("[","")#eliminar parentesis
                    dia = dia.replace("]","")#eliminar parentesis
                    final = dia.split(',')#crear lista
                    i = 0
                    while i < len(final):
                        final[i] = final[i].replace(" ","")
                        final[i+1] = final[i+1].replace(" ","")
                        print(final[i],final[i+1],final[i+2])#imprimir cada día destivo
                        i=i+3
                        while i > len(final):#para evitar errores de index
                            i = i-1
                        
            except:
                print("País o Año no disponible")
    else:
        print("Tipo de datos inválidos")

def determinarCalendarioMes(anno,mes,pais):
    #validacion de tipo de dato
    if isinstance(anno,int) and isinstance(mes,int) and isinstance(pais,str):
        #validar mes
        if (mes >= 1 and mes <= 12):
            #obetener calendario
            cl=calendar.TextCalendar()
            #calendario por mes y año
            calendario=cl.formatmonth(anno,mes)
            
            print(calendario)
            
            #obtener nombre del mes
            mesingles = calendar.month_name[mes]
            
            #traducir a español el mes
            gs = goslate.Goslate()
            mesespa = gs.translate(mesingles, 'es')
            
            #Si tira error urllib.error.HTTPError: HTTP Error 429: Too Many Requests
            switcher = {
                "January":"enero",
                "February":"febrero",
                "March":"marzo",
                "April":"abril",
                "May":"mayo",
                "June":"junio",
                "July":"julio",
                "August":"agosto",
                "September":"septiembre",
                "October":"octubre",
                "November":"noviembre",
                "December":"diciembre"
            }

            #mesespa = switcher.get(mesingles,"nothing")
                

            #Buscar dias fectivos del mes
            #Para el caso de los paises con mas de dos palabras
            if(len(pais.split())>1):
                pais = pais.replace(" ","-")
                my_url = "http://www.cuandoenelmundo.com/calendario/"+pais+"/"+str(anno)
                try:
                    uClient = uReq(my_url)#conección a url    
                    page_html = uClient.read()#obtener datos de url
                    uClient.close()#cerrar coneccion

                    page_soup = soup(page_html,"html.parser")#parsear datos de página
                    hdays = page_soup.find('div',{'class':"hdays"})#buscar seccion de días festivos
                    table = hdays.find_all('table',{'class':"hdays"})#buscar tabla de días destivos
                    #por cada tabla encontrada
                    print("Días festivos en "+pais+" este mes:")
                    print("")
                    for element in table:  
                        dia = element.find_all('td')#fechas encontradas
                        dia = re.sub('<[^>]*>', '', str(dia))#eliminar texto inncesario
                        dia = dia.replace("[","")#eliminar parentesis
                        dia = dia.replace("]","")#eliminar parentesis
                        final = dia.split(',')#crear lista
                        i = 0
                        
                        while i < len(final):
                            final[i] = final[i].replace(" ","")
                            final[i+1] = final[i+1].replace(" ","")
                            if(final[i+1] == mesespa):
                                print(final[i],final[i+1],final[i+2])#imprimir cada día destivo
                            i=i+3
                            while i > len(final):#para evitar errores de index
                                i = i-1
                            
                except:
                    print("País o Año no disponible")
        else:
            print("Número de mes inválido")
    else:
        print("Tipo de dato inválido")

        
def verMensaje():
    host = '';#mi ip
    port = 13000;
    buf = 1024;
    addr = (host, port);
    #conexion con el socket
    UDPSock = socket(AF_INET, SOCK_DGRAM);
    UDPSock.bind(addr);
    print ("Esperando por mensajes...");
    while True:
        #encuentra un mensaje
        (data, addr) = UDPSock.recvfrom(buf);
        print ("Mensaje recibido: " + data.decode('utf-8'));
        break;
    UDPSock.close();


def enviarMensaje(mensaje):
    host = '192.168.1.128'; # ip del que recibe el mensaje
    port = 13000;
    addr = (host, port);
    #conexion con el socket
    UDPSock = socket(AF_INET, SOCK_DGRAM);
    UDPSock.sendto(mensaje.encode('utf-8'), addr);#envia mensaje
    UDPSock.close();
    print("enviado")



