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


