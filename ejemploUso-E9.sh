#!/usr/bin/env bash

«procesoEnBash»

if [ $? -eq 0 ];
then
    python3 envcorreos.py -to "mi_correo@outlook.com" -sub "Resultado" -msj "Proceso exitoso" -file "resultados.res"
else
    python3 envcorreos.py -to "mi_correo@outlook.com" -sub "Resultado" -msj "Proceso no exitoso"
fi

