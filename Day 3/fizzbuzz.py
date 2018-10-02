# https://github.com/adamsaparudin/python-datascience


# if (kondisi)

# if ("adam" == "adam") # True / False

# Task 1
# FIZZBUZZ
# print FIZZ jika bisa dibagi 3,
# print BUZZ jika bisa dibagi 5,
# print FIZZBUZZ jika bisa dibagi 15,
# print angka nya sendiri jika tidak bisa dibagi 3 atau 5

# input 6
# FIZZ

# input 10
# BUZZ

# input 30
# FIZZBUZZ

def print_fizzbuzz(numb):
    if (numb % 15) == 0:
        return "FIZZBUZZ"
    elif (numb % 3) == 0:
        print("FIZZ")
    elif (numb % 5) == 0:
        print("BUZZ")
    else:
        print( numb)

def tambahan(a, b):
  return a + b

def main():
    while True:
        numb = int(input("Input bilangan bulat: "))
        fizz = print_fizzbuzz(numb)
        print(fizz)

main()