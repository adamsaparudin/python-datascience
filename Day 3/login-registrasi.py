import sys

def registrasi():
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    return username, password

def login(username, password): # list_user,
    input_user = input("Masukan username: ")
    input_pass = input("Masukan password: ")
    if username == input_user and password == input_pass:
        print ("Anda berhasil login")
    else:
        print("Salah username dan password")

def print_menu():
    print("Pilih menu untuk melakukan aksi")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

def main():
    # list_user = []
    username = ""
    password = ""
    while True:
        print_menu()
        menu = int(input("Pilihan menu: "))
        if (menu == 1):
            username, password = registrasi()
            # "skks".capitalize() # SKKS
            # list_user.append({'username': username, 'password': password})
        elif (menu == 2):
            login(username, password)
        elif (menu == 3):
            sys.exit()
        else:
            print("Masukan pilihan menu yang benar")

main()