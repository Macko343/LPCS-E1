#!/usr/bin/env bash
ip address
hostname -I

nmap --script default $(hostname -I) 		#nmap al segmento de red privada principal
nmap --script default 192.168.43.* 			#nmap a todo el segmento de mi red privada
nmap -Pn --script vuln $(curl ifconfig.me) 	#nmap de vulnerabilidades a mi red privada
nmap -Pn --script vuln scanme.nmap.org 		#nmap de vulneravilidades a scanme de nmap
