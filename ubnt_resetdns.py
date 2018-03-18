#!/usr/bin/python

#
# Author: Yoel Antonio Duran Diaz <yoet92@gmail.com>
# Git: https://github.com/yoet92/ubnt_resetdns.git
#

import paramiko
import os

ssh_servidor = '192.168.1.20'
ssh_usuario  = 'ubnt'
ssh_clave    = 'ubnt'
ssh_puerto   = 22
server_dns   = '190.6.81.226'
comando      = 'udhcpc -i ath0 -s /var/etc/udhcpc/udhcpc >/dev/null'
request      = os.system("nslookup " + server_dns)

if request == 0:
	print ("Response OK ..")
else:
	conexion = paramiko.Transport((ssh_servidor, ssh_puerto))
	conexion.connect(username = ssh_usuario, password = ssh_clave)
	canal = conexion.open_session()
	canal.exec_command(comando)
	conexion.close()
	print ("DNS Renovado ..")
