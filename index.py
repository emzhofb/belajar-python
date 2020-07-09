# # tipe data Boolean
# print(True)

# # tipe data String
# print("Ayo belajar Python")
# print("Belajar Python Sangat Mudah")

# # tipe data Integer
# print(20)

# # tipe data Float
# print(3.14)

# # tipe data Hexadecimal
# # print(9a)

# # type data Complex
# print(5j)

# # type data List
# print([1, 2, 3, 4, 5])
# print(["satu", "dua", "tiga"])

# # type data Dictionary
# print({ "name": "John", "age": 23 })

# biodata = {
#   "name": "Ikhda",
#   "age": 21
# }
# print(biodata)
# print(type(biodata))

# # proses memasukkan data ke dalam variable
# nama = "John Doe"
# # proses mencetak variable
# print(nama)

# # nilai dan tipe data dalam variable dapat di ubah
# umur = 20
# print(umur)
# print(type(umur))
# umur = "dua puluh satu"
# print(umur)
# print(type(umur))

# namaDepan = "Budi"
# namaBelakang = "Susanto"
# nama = namaDepan + " " + namaBelakang
# umur = 22
# hobi = "Berenang"
# print("Biodata\n", nama, "\n", umur, "\n", hobi)

# # contoh variable lainnya
# inivariable = "Halo"
# ini_juga_variable = "Hai"
# _inivariablejuga = 'Hi'
# inivariable222 = 'Bye'

# panjang = 10
# lebar = 5
# luas = panjang * lebar
# print(luas)

# operator aritmatika

# # penjumlahan
# print(13 + 2)
# apel = 7
# jeruk = 9
# buah = apel + jeruk
# print(buah)

# # pengurangan
# hutang = 10000
# bayar = 5000
# sisaHutang = hutang - bayar
# print('Sisa hutang', sisaHutang)

# # perkalian
# panjang = 15
# lebar = 8
# luas = panjang * lebar
# print(luas)

# # pembagian
# kue = 16
# anak = 4
# print('Setiap anak akan mendapat', kuePerAnak)
# kuePerAnak = kue / anak

# # sisa bagi / modulus
# bilangan1 = 14
# bilangan2 = 5
# hasil = bilangan1 % bilangan2
# print('sisa bagi', hasil)

# # pangkat
# bilangan3 = 8
# bilangan4 = 2
# hasilPangkat = bilangan3 ** bilangan4
# print(hasilPangkat)

# # pembagian bulat
# print(10//3)

# # if
# nilai = 9
# if (nilai > 7):
#   print('lebih dari 7')

# # if else
# nilai = 3
# if (nilai > 7):
#   print('selamat anda lulus')
# else:
#   print('maaf anda tidak lulus')

# # if elif
# hari = 'minggu'
# if (hari == 'senin'):
#   print('saya akan kerja')
# elif (hari == 'selasa'):
#   print('kuliah')
# elif (hari == 'minggu'):
#   print('libur')

# # while loop
# count = 0
# while (count < 9):
#   print("The count is:", count)
#   count = count + 1

# print("good bye!")
# # for loop
# angka = [1, 2, 3, 4, 5]
# for x in angka:
#   print(x)

# buah = ['nanas', 'apel', 'jeruk']
# for makanan in buah:
#   print('saya suka makan:', makanan)

# # nested loop
# i = 2
# while(i < 100):
#   j = 2
#   while(j <= (i/j)):
#     if not(i%j): break
#     j = j + 1
#   if (j > i/j): print(i, 'is prime')
#   i = i + 1

# print('good bye!')

# # string
# name = 'John Doe'
# message = 'John Doe learning python'

# print('name[0]:', name[0])
# print('message[1:4]:', message[1:4])

# message = 'Hello World'
# print('updated string:', message[:6] + 'Python')

# print ("My name is %s and weight is %d kg!" % ('Zara', 21))

# kutipantiga = """this is a long string that is made up of
# several lines and non-printable characters such as
# TAB ( \t ) and they will show up that way when displayed.
# NEWLINEs within the string, whether explicitly given like
# this within the brackets [ \n ], or just a NEWLINE within
# the variable assignment will also show up.
# """
# print (kutipantiga)

# # list
# list1 = ['kimia', 'fisika', 1993, 2017]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# list3 = ['a', 'b','c', 'd']

# print('list1[1]:', list1[1])
# print('list2[1:5] :', list2[1:5])

# print('sebelum di update:', list3[2])
# list3[2] = 'e'
# print('setelah di update:', list3[2])

# print('sebelum di hapus:', list3)
# del list3[2]
# print('setelah di hapus:', list3)

# for x in [1,2,3]:
#   print(x,end = ' ')

# # dictionary
# dictionary = {
#   'name': 'zara',
#   'age': 7,
#   'class': 'first'
# }

# print(dictionary)
# print(dictionary['name'])
# dictionary['school'] = 'erangel school'
# print(dictionary)
# del dictionary['class']
# print(dictionary)
# dictionary.clear()
# print(dictionary)
# del dictionary

# # time
# import time

# ticks = time.time()
# print('berjalan sejak', ticks)
# localtime = time.localtime(time.time())
# print('waktu lokal saat ini', localtime)
# localtime = time.asctime(time.localtime(time.time()))
# print('waktu lokal saat ini', localtime)

# import calendar
# cal = calendar.month(2008, 1)
# print(cal)

# # function
# def printme(str):
#   'this prints are passed string into this function'
#   print(str)
#   return

# printme('test')

# # class
# class Employee:
#   'common base class'
#   empCount = 0

#   def __init__(self, name, salary):
#     self.name = name
#     self.salary = salary
#     Employee.empCount += 1

#   def displayCount(self):
#     print('Total employee', Employee.empCount)
  
#   def displayEmployee(self):
#     print('name', self.name, 'salary', self.salary)

# emp1 = Employee('Zara', 2000)
# emp1.displayEmployee()
