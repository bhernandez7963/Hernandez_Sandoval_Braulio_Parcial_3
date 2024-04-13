import sys
import subprocess
import platform
import json

sistema = platform.system()
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
    version = platform.win32_ver()
else:
    local = subprocess.getoutput("ifconfig | grep 'inet' | grep -Fv 192.168.159.1 | awk '{print $2}'")
    version = platform.uname()

hostname = platform.node()
cpu = platform.processor()

diccionario = {'ip': local, 'so': sistema, 'version': version, 'hostname': hostname, 'cpu': cpu}
#dictionaryToJson = json.dumps(diccionario)
#print(dictionaryToJson)
file = open("file.json", "w")
json.dump(diccionario, file,indent=4)