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

