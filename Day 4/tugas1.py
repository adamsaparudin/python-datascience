import os
import json

def write_to_db(dbfile, siswa_dict):
  db = open(dbfile, "w")

  db.write(db)
  return

def main_menu():
  print("1. Registrasi Siswa")
  print("2. Input Nilai Siswa")
  print("3. Tampilkan Data Siswa")
  input_menu = int(input("Pilih menu: "))
  return input_menu

def menu_registrasi(dbfile):
  nama = input("Input Nama Siswa: ")
  kelas = input("Input Kelas Siswa: ")
  db = json.load(open(dbfile))
  if db["siswa"].get(kelas) != None:
    db["siswa"][kelas].append({"nama": nama})
  else:
    print("masuk sini")
    db["siswa"][kelas] = []

    db["siswa"][kelas].append({"nama": nama})
  db_save = open(dbfile, "w")
  db_save.write(json.dumps(db))
  db_save.close()
  return

def get_siswa_index(kelas, nama):
  for index, siswa in enumerate(kelas):
    if siswa["nama"] == nama:
      return index
  return -1

def hitung_nilai_rata_rata(kelas):
  total = 0
  for siswa in kelas:
    if siswa.get("nilai") != None:
      total += siswa["nilai"]
  return total / len(kelas)

def menu_input_nilai(dbfile):
  kelas = input("Input Kelas: ")
  nama = input("Input Nama: ")
  nilai = input("Input Nilai: ")
  db = json.load(open(dbfile))
  if db["siswa"].get(kelas) != None:
    idx_siswa = get_siswa_index(db["siswa"][kelas], nama)
    if idx_siswa >= 0:
      db["siswa"][kelas][idx_siswa]["nilai"] = int(nilai)
      db["nilai_rata_rata"][kelas] = hitung_nilai_rata_rata(db["siswa"][kelas])
  db_file = open(dbfile, "w")
  json.dump(db, db_file, indent=4, sort_keys=True)
  return

def menu_data_siswa(dbfile):
  db = open(dbfile)
  print(json.load(db))

def main():
  dbfile = "siswa.json"
  while True:
    input_menu = main_menu()
    if input_menu == 1:
      menu_registrasi(dbfile)
    elif input_menu == 2:
      menu_input_nilai(dbfile)
    elif input_menu == 3:
      menu_data_siswa(dbfile)
main()