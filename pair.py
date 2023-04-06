vize = float(input("Vize notunu giriniz"))
final =float(input ("final notunuzu giriniz"))
ortalama = (vize*0.4)+(final*0.6)

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if final < 40:
    print("Kullanıcı kaldı")
elif ortalama < 50:
    print("Kullanıcı kaldı")
elif vize == final*2:
    print("Kullanıcı kaldı")
else:
    print("Kullanıcı geçti")

#karar yapıları -end