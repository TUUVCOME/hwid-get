import os
from wmi import WMI
import getpass
username = getpass.getuser()
a = WMI().Win32_ComputerSystemProduct()[0].UUID

b = input(f"Ваш HWID - {a}\n1. Сохранить в txt файл\n2. Перезаписать\n3. Выход\n")

def ensure_file_exists():
    if not os.path.isfile("hwid.txt"):
        with open("hwid.txt", "w") as f:
            f.write("")

def hwid_seek():
    with open("hwid.txt", "r+") as f:
        return f.read()

if b == "1":
    ensure_file_exists()
    hwid = hwid_seek()
    if not hwid:
        with open("hwid.txt", "w", encoding="UTF-8") as file_out:
            file_out.write(f"{a}\n")
            print(f"HWID сохранен в файл - hwid.txt по пути C:/Users/{username}\n")
    else:
        print("Вам не нужно сохранять HWID, он у вас уже сохранён!\n")

elif b == "2":
    ensure_file_exists()
    with open("hwid.txt", "w", encoding="UTF-8") as file_out:
        file_out.write(f"{a}\n")
        print(f"HWID сохранен в файл - hwid.txt по пути C:/Users/{username}\n")
elif b == "3":
    os.system("break")
    
else:
    print("Вы ввели не существующую команду!\n")
    os.system("break")
