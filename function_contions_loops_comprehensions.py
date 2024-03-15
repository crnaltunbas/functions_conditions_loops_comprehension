#  Fonksiyonlar, Koşullar, Döngüler, Comprehensions


#  Fonksiyonlar (Functions)
#  Belirli görevleri yerine getirmek üzere yazılan kod parçalarıdır.

#  Fonksiyon okuryazarlığı

print("a")
?print
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


