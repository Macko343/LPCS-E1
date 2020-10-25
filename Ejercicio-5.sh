#!/usr/bin/env bash

#Hay que tener la lista de los valores md5 de cada archivo, en un archico checksum.txt
if [ $(grep -c "$(md5sum msg.txt)" checksum.txt) -eq 1 ]
then 
	echo "msg.txt esta integro"
	cat msg.txt | base64 > msg_codificado.txt
else
	echo "msg.txt esta corrupto y no se ha codificado"
fi

if [ $(grep -c "$(md5sum fcfm.png)" checksum.txt) -eq 1 ]
then 
	echo "fcfm.png esta integro"
	cat fcfm.png | base64 > fcfm_codificado.txt
else
	echo "fcfm.png esta corrupto y no se ha codificado"
fi

if [ $(grep -c "$(md5sum mystery_img1.txt)" checksum.txt) -eq 1 ]
then 
	echo "mystery_img1.txt esta integro"
	cat mystery_img1.txt | base64 --decode > mystery_img1.png
else
	echo "mystery_img1.txt esta corrupto y no se ha decodificado"
fi

if [ $(grep -c "$(md5sum mystery_img2.txt)" checksum.txt) -eq 1 ]
then 
	echo "mystery_img2.txt esta integro"
	cat mystery_img2.txt | base64 --decode > mystery_img2.png
else
	echo "mystery_img2.txt esta corrupto y no se ha decodificado"
fi
