import database
import utils
import books

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Barcha kitoblarni korish")
    print("2. Kitob qoshish")
    print("3. Kitob malumotlarini tahrirlash")
    print("4. Kitobni ochirish")
    print("5. Kitob qidirish")
    print("6. Kitobni foydalanuvchiga berish")
    print("7. Kitobni qaytarish")
    print("8. Mavjud kitoblarni korish")
    print("9. Berilgan kitoblarni korish")
    print("0. Chiqish")
    
    tanlov = input("Tanlang: ").strip()
    
    if not tanlov:
        continue
    
    if tanlov == '1':
        books.kitoblarni_korish()
    elif tanlov == '2':
        books.kitob_qoshish()
    elif tanlov == '3':
        books.kitob_tahirlash()
    elif tanlov == '4':
        books.kitob_ochirish()
    elif tanlov == '5':
        books.kitob_qidirish()
    elif tanlov == '6':
        books.kitob_berish()
    elif tanlov == '7':
        books.kitob_qaytarish()
    elif tanlov == '8':
        books.mavjud_kitoblar()
    elif tanlov == '9':
        books.berilgan_kitoblar()
    elif tanlov == '0':
        print("Dastur yakunlandi. Xayr!")
        break
    else:
        print("Xatolik: Noto'g'ri tanlov! Iltimos, 0 dan 9 gacha son kiriting.")