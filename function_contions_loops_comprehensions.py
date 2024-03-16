 #  Fonksiyonlar, Koşullar, Döngüler, Comprehensions


#  Fonksiyonlar (Functions)
#  Belirli görevleri yerine getirmek üzere yazılan kod parçalarıdır.

#  Fonksiyon okuryazarlığı

print("a")

#  Argümanlar fonksiyonalrın genel amacını biçimlendirmek üzere kullanılan alt görevcilerdir.
print("a",  "b")

print("a",  "b", sep="__")
help(print)


#  Fonksiyon Tanımlama
# Girilen sayıları iki ile tanımlayacak bir fonksiyon tanımlayalım.


def calculate(x):
  "def ile fonksiyon oluşturacağımız bildirildi, fonksiyon adlandırıldı argüman olarakta x verildi."
  print(x*2)

calculate(5)

"İki argümanlı/parametreli bir fonksiyon tanımlayalım."


def summer(arg1, arg2):
  print(arg1 + arg2)

summer(7, 8)


#  Docstring
#  Bir fonksiyonda ürettiğimizde fonksiyonun ne işe yaradığını anlayabilmek için ortak bir dilde oluştu yazıdır.
#  Docstring tarzında numpy için veya google için oluşturulmak isteniyorsa ayarlarda tools kısmından bu değiştirilebilir

def summer(arg1, arg2):

  """
   Sum of two numbers
  :param arg1:int, float

  :param arg2:int, float

  :return: int, float

  :Examples: Burada örnek verebilirsiniz.

  :Notes: Burada bu fonksiyonun nerede kullanıldığını yazabilir ihtiyaç duyduğunuz notları yazabilirsiniz

  """

  print(arg1 + arg2)

summer(1, 3)


#  Fonksiyonların(Statement/Body Bölümü)
#  Fonksiyonların ne görevi yapacğına hangi sırayla hangi şekilde yapılacağına karar verdiğimiz ve bunu pythona ifade
#  ettiğimiz önemli olan bölümdür.
#  def function_name(parameters/arguments): parametre /argüman her zaman olmayabilir bir fonksiyonda.
#  statements(function body)

def say_hi(string):
  print(string)
  print("hi")
  print("merhaba")

say_hi("Ceren")
def multiplication(a, b):
  c = a * b
  print(c)

multiplication(10, 9)


# Girilen değerleri bir liste içine saklayacak fonksiyon yazalım.

list_store = []

def add_element(a, b):
  c = a * b
  list_store.append(c)
  print(list_store)

add_element(1, 8)

add_element(18, 20)

add_element(19, 50)


#  Ön Tanımlı Argümanlar/ Parametreler(Default Parameters / Arguments)
#  Parametrele, fonksiyonların tanımlanması esnasında kullanılan ifadelerdir.
#  Bu parametreler fonksiyonun çağrılması esnasında bir değer aldığında argüman olarak anılır.

def divide(a, b):
  print(a / b)

divide(1, 2)

def divide(a, b=1):
  print(a / b)

divide(1)

def say_hi(string="Selam"):
  print(string)
  print("hi")
  print("merhaba")

say_hi()

def say_hi(string="Selam"):
  print(string)
  print("hi")
  print("merhaba")

say_hi("Ceren")

#  Ne zaman fonksiyon yazma ihtiyacınız olur?

#  Dry prensibi : kendini tekrar etme

def calculate(varm, moisture, charge):
  print((varm + moisture)/charge)

calculate(98, 12, 78)


#  Return:Fonksiyon çıktılarını girdi olarak kullanmak

def calculate(varm, moisture, charge):
  print((varm + moisture)/charge)

#calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
   return((varm + moisture)/charge)

calculate(98, 12, 78) * 10
a = calculate(98, 12,78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

calculate(98,12, 78)

type(calculate(98,12, 78))

varm, moisture, charge, output = calculate(98, 12, 78)

calculate(98, 12, 78) * 10


#  Fonksiyon içerisinden fonksiyon çağırmak

def calculate(varm, moisture, charge):
  return int((varm + moisture) / charge)

calculate(98, 12, 78) * 10

def standardization(a, p):
  return a * 10 / 100 * p * p
standardization(45, 1)


def all_calculation(varm, moisture, charge, p):
  a = calculate(varm, moisture, charge)
  b = standardization(a, p)
  print(b * 10)

all_calculation(1, 3, 5, 12)

def all_calculation(varm, moisture, charge, a, p):
  print(calculate(varm, moisture, charge))
  b = standardization(a, p)
  print(b * 10)

all_calculation(1, 3, 5,19, 12)


#  Local ve Global Değişkenler (Local & Global Variables)

list_store = [1, 2]

def add_element(a, b):
  c = a * b
  list_store.append(c)
  print(list_store)

add_element(1, 9)

#  Burada list_store global değişkendir. Ama c yerel etki alanında olduğundan local değişkendir.

#  Koşullar (Conditions)

#  True- False' u hatırlayalım

1 == 1
1 == 2

#  if
#  Sadece koşul sağlandığında eylem gerçekleşir.

if 1 == 1:
  print("something")

number = 11
if number == 10:
  print("number is 10")

number = 10
number = 20

def number_check(number):
  if number == 10:
    print("numbers is 10")

number_check(12)

# else
# if koşulu sağlanmadığında yapılacak eylemi gösterir.

def number_check(number):
  if number == 10:
    print("numbers is 10")
  else:
    print("number is not 10")

number_check(12)


#  elif
#  if koşulu sağlanmazsa başka bir şartı sağlamak için elif komutu kullanılır.elif -teki şart sağlanmazsa else- deki
 #  eylemi gerçekleştirir.

def number_check(number):
  if number > 10:
    print("greater than 10")
  elif number < 10:
    print("less than 10")
  else:
    print("equal to 10")

number_check(11)


#  Döngüler (Loops)

#  for loop
students = ["John", "Mark", "Vanessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
  print(student)



for student in students:
  print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
  print(salary)



for salary in salaries:
  print(int((salary * 20/100 + salary)))


def new_salary(salary, rate):
  return int(salary * rate/100 + salary)

new_salary(1500, 10)

for salary in salaries:
  print(new_salary(salary, 10))



# maaşı 3000 tl olanlar ,3000 tl den küçük olanlar ve 3000 tl den büyük olanlara uygulanacak farklı zamlar sonucu
 # maaşları hesaplayalım. Bu kısımda tekrarlayan uzun fonksiyonlar ile işlem yaptık.
# Kendi yaptığım algoritma
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
  if salary > 3000:
     print(int((salary * 10/100) + salary))
  elif salary == 3000:
    print(int((salary * 20/100) + salary))
  else :
    print(int((salary * 30/100) + salary))

# Aşağıdaki kısımda kısa yoldan fonsiyon üreterek kod yazdık.

def new_salary(salary, rate):
  return int(salary * rate/100 + salary)

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
  if salary > 3000:
     print(new_salary(salary, 10))
  elif salary == 3000:
    print(new_salary(salary, 20))
  else :
    print(new_salary(salary, 30))




#  Uygulama Mülakat sorusu
# Avrupada bir üniversitenin doktara departmanına alınacak öğrenciye sorulan mülakat sorusudur.
# Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
# Before : "hi my name is john and i am learning python"
# After : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
# Aslında dikkatli baktığımızda indexleri çift olan elemanlar büyük olsun, tek olan elemanlar küçük olsun.

# Bu örnekte range fonksiyonunu kullanacağız. Bizim yukarıdaki ifadeyi yapabilmek için stringin bütün indexleri boyunca
# Gezip tekse küçültüp çiftse büyültmemiz gerekiyor.Range fonksiyonun kullanımını aşağıdaaki gibi açıklayabiliriz


string = "hi my name is john and i am learning python"
range(len(string))
range(0, 43)

for i in range(len(string)):
  print(i)


def alternating(string):
    new_string = ""
    # girilen string'in indexlerinde gez.
    for string_index in range(len(string)):
        # İndex çift ise büyük harfe çevir
        if string_index % 2 == 0:
          # % mod alma işaretidir.
            new_string += string[string_index].upper()
        # İndex tek ise küçük harfe çevir.
        else:
          new_string += string[string_index].lower()
    print(new_string)
alternating("hi my name is john and i am learning python")


#  break & continue & while

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
  if salary == 3000:
    break
    print(salary)

    # istenen şart sağladığında döngü durur.(break)

for salary in salaries:
  if salary == 3000:
    continue
    print(salary)

    # istenen şart sağlandığında diğer elemana geç.(continue)

# while (dığı sürece)
number = 1
while number < 5:
  print(number)
  number += 1

  # number 5' ten küçük olduğu sürece döngü devam eder.


#  Enumerate : Otomatik counter / indexer ile for loop
#  Gezilebilir bir yapı içerisinde gezerken aynı zamanda index bilgileerinide tutup gerekirse bu indexlere görede işlem
#  yapmamızı sağlayan yapıdır.


students = ["John", "Mark", "Vanessa", "Mariam"]
for student in students:
  print(student)

A = []
B = []
for index, student in enumerate(students):
  if index % 2 == 0:
    A.append(student)
  else:
    B.append(student)

print(A)
print(B)



# Uygulama - Mülakat sorusu
# divide_ students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri bir başka listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Vanessa", "Mariam"]


def divide_students(students):
  groups = [[], []]
  for index, student in enumerate( students):
    if index % 2 == 0 :
      groups[0].append(student)
    else:
      groups[1].append(student)
  print(groups)
  return

divide_students(students)


#  alternating fonksiyonun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
      if i % 2 == 0:
        new_string += letter.upper()
      else:
        new_string += letter.lower()
    print(new_string)
alternating_with_enumerate("hi my name is john and i am learning python")

# Zip

# Ayrı listeleri tek bir liste içerisine her birisinde bulunan elemanları aynı sırada eşleyerek bir araya getirip
 # herbirini tek eleman gibi gösterir.
students = ["John", "Mark", "Vanessa", "Mariam"]

departments = ["math", "static", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students,departments,ages))


# lambda, map, filter, reduce

#  lambda kullan at fonksiyondur. Tanımlama gerekmez.

def summer(a, b):
  return a + b
summer(1, 3) * 9

new_sum = lambda a, b: a + b
new_sum(4, 5)

# map
# İçinde gezebileceğin nesne ve buna uygulayacağımız fonksiyonu verdiğimizde otamatik olarak verilen nesnenin bütün
# elemanlarına uygular. for döngüsü yazmaktan kurtarır.


salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
  return x * 20/100 + x

list(map(new_salary, salaries))


# YA DA LAMPDAYI KULLANARAK

list(map(lambda x: x *20 / 100 + x, salaries))


# filter
# Belirli bir koşulu sağlamak istemeyenleri ayırıyor. Sorgu bölümü gibi düşünülmelidir.

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x:x % 2 ==0, list_store))

# Reduce
# İteratif bir elemana istenilen işlemi uygulamak
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)




# COMPREHENSİONS

# List Comprehension

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(salary):
  return (salary * 20 / 100 + salary)


null_list = []
for salary in salaries:
  null_list.append(new_salary(salary))

null_list = []
for salary in salaries:
  if salary > 3000:
    null_list.append(new_salary(salary))
  else:
    null_list.append(new_salary(salary * 2))
print(null_list)

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

#  salaries listesindeki her her salary-i  iki ile çarpacağımızı düşünelim.
[salaries * 2 for salary in salaries]

[salaries * 2 for salary in salaries if salary < 3000]

[new_salary(salaries * 2) if salary < 3000 else new_salary(salary * 0.2)for salary in salaries ]
#  DİKKAT  COMPREHENSİONS BAŞLIĞINDAN İTİBAREN BU SATIRA KADAR  BİR HATA VAR NEYDEN KAYNAKLANDIĞINI ÇÖZEMEDİM !!!!

# Eğer tek başına bir if kullanıyorsak bu en sağ tarafta olmalıdır. Eğer if ve else ifadesini birlikte kullanacaksak,
# for ifadesi en sağda yer almalıdır.



students = ["John", "Mark", "Vanessa", "Mariam"]

students_no = ["John", "Vanessa"]

[student.lower() if student in students_no else student.upper() for student in students]


# Dict Comprehension

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
dictionary.keys()
dictionary.items()
dictionary.values()

#  Bu sözlük içerisinde her bir value- nun karesini almak istiyoruz.Ancak key-lere dokunmayacağız.

{k: v **2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}


# Uygulama- Mülakat sorusu Dict comprehensions

# Amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key-ler orjinal değerler value-lar ise değiştirilmiş değerler olacak.


numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
       new_dict[n] = n **2
print(new_dict)
{n: n ** 2 for n in numbers if n % 2 ==0}



# List & Dict Comprehension Uygulamalar

# Bir veri setindeki değişken isimlerini değiştirmek

# before
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_losses', 'abbrev']

# after
#  ['TOTAL', 'SPEEDİNG', 'ALCOHOL', 'NOT_DİSTRACTED', 'NO_PREVİOUS', 'INS_LOSSES', 'ABBREV']

#  aşağıda bir kütüphane import edilecek ama ana konumuz şu an o olmadığı için çok takılmadık.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
  print(col.upper())

A = []
for col in df.columns:
  A.append(col.upper())
print(A)


df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


# İsminde " INS " olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.

# before:
# ['TOTAL',
# 'SPEEDİNG',
# 'ALCOHOL',
# 'NOT_DİSTRACTED',
# 'NO_PREVİOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDİNG',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DİSTRACTED',
# 'NO_FLAG_NO_PREVİOUS',
# 'FLAG_INS_PREMIUM',
# 'FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV'

[col for col in df.columns if "INS" in  col]

["FLAG_" + col for col in df.columns if "INS" in  col]

["FLAG_" + col if "INS" in  col else "NO_FLAG" + col for col in df.columns ]

df.columns = ["FLAG_" + col if "INS" in  col else "NO_FLAG" + col for col in df.columns ]


# Amaç key-i string, value-su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.

# Output:
#{'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
#'ins_losses': ['mean', 'min', 'max', 'var']}


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}
agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols:
  soz[col] = agg_list

# kısa yol
{col: agg_list for col in num_cols}



# ek olarak
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()
df[num_cols].agg(new_dict)

