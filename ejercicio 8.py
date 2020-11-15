#!/usr/bin/env python3

from ftplib import FTP, FTP_PORT
import argparse


def buscarDirectorios(conexion,folders):
    for Dir in folders:
        fEnc = []
        ls = []
        directorios = []
        conexion.retrlines(f'LIST /{Dir}', ls.append)
        for nom in ls:
            if nom.startswith('dr'):
                directorios.append(nom)
        for nom in directorios:
            Folders.append(f'{Dir}/'+str(nom).rsplit(' ')[-1].replace("']",''))
            fEnc.append(f'{Dir}/'+str(nom).rsplit(' ')[-1].replace("']",''))
            dires = fEnc
    if len(directorios)>0:
        buscarDirectorios(conexion,dires)
        
def obtenerTextos(conexion, folders):
    ls = []
    lText = []
    for Dir in folders:
        conexion.retrlines(f'LIST {Dir}', ls.append)
    for nom in ls:
        if str(nom).rsplit('.')[-1] in ['msg','txt','README']:
            lText.append(f'{Dir}/'+str(nom).rsplit(' ')[-1])    
    return lText

def descargarArchivos(conexion, listaRemota, pathLocal):
    for file in listaRemota:
        with open(f"{pathLocal}/{str(file).rsplit('/')[-1]}",'wb') as f:
            conexion.retrbinary(f"RETR {file} ", f.write)
        f.close()


def main(servidor, ruta, puerto):
     
    ftp = FTP(servidor)
    ftp.login()
    global Folders
    Folders = ['/']
        
    buscarDirectorios(ftp, Folders)
    descargarArchivos(ftp, obtenerTextos(ftp, Folders), ruta)


    
if __name__ == "__main__":
    description = """Ejemplo de Uso:
        -ser "ftp.us.debian.org" -path "/home/jhernandez" -key
    """
    parser = argparse.ArgumentParser(description='Descargar archivos txt, msg,\
                                     README', epilog=description,
                                     formatter_class=argparse.
                                     RawDescriptionHelpFormatter)
    parser.add_argument("-ser", metavar='Servidor', dest="ser", help="Servidor\
                        ftp", required=True)
    parser.add_argument("-path", metavar='Ruta', dest="path", help="Ruta del \
                        directorio para guardar los archivos descargados", 
                        required=True)
    parser.add_argument("-port", metavar='Puerto', dest="port", help="Puerto de\
                        enlace")
    
    servidor = parser.parse_args().ser
    ruta = parser.parse_args().path
    puerto = parser.parse_args().port #No se utiliza el puerto en este script
    
    main(servidor, ruta, puerto)
	


