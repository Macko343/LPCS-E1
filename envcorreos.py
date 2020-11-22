#!/usr/bin/env python3

import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import json


def loggin(usuario, contra):
    eSesion = smtplib.SMTP('smtp.office365.com:587')
    eSesion.starttls()
    eSesion.login(usuario, contra)
    return eSesion

def crearMensaje(de, para, asunto, msj, adjunto):
    msg = MIMEMultipart()
    mensaje = msj
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje,'plain'))
    if adjunto is not None:
        f = open(adjunto,'rb')
        obj = MIMEBase('application','octet-stream')
        obj.set_payload(f.read())
        encoders.encode_base64(obj)
        obj.add_header('Content-Disposition',"attachment; filename= "+adjunto)
        msg.attach(obj)
    miMsj = msg.as_string()
    return miMsj

def enviarMensaje(sesion, de, para, mensaje):
    sesion.sendmail(de, para, mensaje)
    sesion.quit()

def main():
    cred = {}
    with open('credentials.json') as f:
        cred = json.load(f)
    f.close()
    usuario = cred['user']
    contra = cred['pass']
    sesion = loggin(usuario, contra)
    miMsj = crearMensaje(usuario, para, asunto, msj, adjunto)
    enviarMensaje(sesion, usuario, para, miMsj)


if __name__ == "__main__":
    description = """Ejemplo de Uso:
        -to "ejemplo@dominio.com" -sub "Hola" -msj "Hola carino" -file "im.png"
    """
    parser = argparse.ArgumentParser(description='Enviar mensajes por correo',
                                    epilog=description,formatter_class=argparse.
                                    RawDescriptionHelpFormatter)
    parser.add_argument("-to", metavar='Para', dest="to", help="Para quien es \
                        el correo", required=True)
    parser.add_argument("-sub", metavar='Asunto', dest="sub", help="Asunto del \
                        mensaje", required=True)
    parser.add_argument("-msj", metavar='Mensaje', dest="msj", help="Mensaje a \
                        enviar", required=True)
    parser.add_argument("-file", metavar='Archivo', dest="file", help="Archivo \
                        para adjuntar al envio")                        
    
    para = parser.parse_args().to
    asunto = parser.parse_args().sub
    msj = parser.parse_args().msj
    adjunto = parser.parse_args().file
    
    main()
