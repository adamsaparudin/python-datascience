# Rangkuman Materi

## File

### membuka file
`fileku = open("myfile.txt")` # apabila hanya 'read' bisa dilakukan tanpa memberi argument kedua.

### menulis file
```python
person_file = open('person.json', 'w') # Karena melakukan operasi write/input maka kita harus memberi argument kedua, yaitu input
person_file.write("nama: Adam Saparudin")
```

### json
```python
import json # kita harus import package json terlebih dahulu.
person = dict(nama="Adam S", umur=23, hobi=["renang", "mandi"])
person_json = json.dumps(person) # method dumps digunakan untuk mengubah dictionary menjadi json

person_dict = open(json.load("person.json")) # method ini kita akan mengimport json menjadi dict
person_dict["favorite_food"] = ["rendang", "ayam bakar"]
person_file = open("person.json", "w")
person_file.write(json.dumps(person_dict)) # apabila kita ingin menulis dict kedalam json, kita harus melakukan operasi dumps terlebih dahulu.

```

### while loop
perulangan/looping menggunakan `while` bisa kita lakukan dengan cara seperti ini.
```python
while True:
    print("ctrl + c, to stop me")

i = 0
while i < 5:
    print(i, end=", ")
    i += 1
# 1, 2, 3, 4, 5,
```

### for loop
contoh perulangan lainnya adalah for loop, biasa digunakan untuk me loop variable atau data dalam bentuk list/tuple
```python
grup_c = ["Andre", "Annisa", "Ayu", "Rian"]
for nama in grup_c:
    print(nama)
# Andre
# Annisa
# Ayu
# Rian
```

