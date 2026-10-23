import database
import utils


def kitoblarni_korish():
    print("\n--- BARCHA KITOBLAR ---")
    utils.royxat_chiqarish(database.books)


def kitob_qoshish():
    print("\n--- KITOB QOSHISH ---")

    nomi = utils.matn_olish ("Kitob nomini kriting: ")
    muallif = utils.matn_olish ("Muallifni kiriting: ")
    yil = utils.son_olish ("Chop etilgan yilini kiriting: ")

    yangi_kitob = {
        "id" : database.next_book_id,
        "title" : nomi,
        "author" : muallif,
        "year" : yil,
        "available" : True

    }

    database.books.append(yangi_kitob)
    database.next_book_id += 1

    print("Kitob muvaffaqiyatli qo'shildi")


def kitob_tahirlash():
    print("\n--- Kitobni tahrirlash ---")

    kitob_id = utils.son_olish("Kitob ID si: ")
    kitob = utils.kitob_topish(kitob_id)

    if not kitob:
        print("Bunday ID dagi kitob topilmadi!")
        return

    print("Agar ma'lumotnoi o'zgartirishni xohlamasangiz, 'Enter'ni bosing")

    yangi_nom = input(f" Yangi nom ({kitob['title']}): ").strip()
    if yangi_nom:
        kitob["title"] = yangi_nom

    yangi_muallif = input(f"Yangi muallif ({kitob['author']}): ").strip()
    if yangi_muallif:
        kitob['author'] = yangi_muallif

    yangi_yil = input(f"Yangi yil ({kitob['year']}): ").strip()
    if yangi_yil.isdigit():
        kitob["year"] = int(yangi_yil)

    print("Kitob ma'lumotlari yangilandi!")


def kitob_ochirish():
    print("\n--- KITOBNI O'CHIRISH ---")
    
    kitob_id = utils.son_olish("O'chiriladigan kitob ID sini kiriting: ")
    kitob = utils.kitob_topish(kitob_id)
    
    if not kitob:
        print("Xatolik: Bu ID dagi kitob topilmadi!")
        return
    
    # Agar kitob kimdadir bo'lsa (berilgan bo'lsa), o'chirishga ruxsat bermaymiz
    if not kitob["available"]:
        print("Xatolik: Bu kitob hozirda foydalanuvchida, uni o'chirib bo'lmaydi!")
        return
    
    database.books.remove(kitob)
    print("Kitob muvaffaqiyatli o'chirildi!")


def kitob_qidirish():
    print("\n--- KITOB QIDIRISH ---")
    
    soz = utils.matn_olish("Qidirilayotgan kitob nomi yoki muallifini kiriting: ").strip().lower()
    
    natijalar = []
    for kitob in database.books:
        # Kiritilgan so'z kitob nomida yoki muallifida bor-yo'qligini 'in' orqali tekshiramiz
        if soz in kitob["title"].lower() or soz in kitob["author"].lower():
            natijalar.append(kitob)
            
    utils.royxat_chiqarish(natijalar)


def kitob_berish():
    print("\n--- KITOB BERISH ---")

    kitob_id = utils.son_olish("Beriladigan kitob ID si: ")
    kitob = utils.kitob_topish(kitob_id)

    if not kitob:
        print("Bu ID dagi kitob topilmadi!")
        return

    if not kitob['available']:
        print("Bu kitob allaqachon boshqa faoydalanuvchiga berilgan!")
        return

    kitob ["available"] = False
    print("Kitob foydalanuvchiga berildi")


def kitob_qaytarish():
    kitob_id = utils.son_olish("Qaytariladigan kitob ID si: ")
    kitob = utils.kitob_topish(kitob_id)

    if not kitob:
            print("Bu ID dagi kitob topilmadi!")
            return
    
    if kitob['available']:
        print("Kitob allaqachon kutubxonada mavjud! (berilmagan)")
        return
    
    kitob ["available"] = True
    print("Kitob muvaffaqiyatli qaytarib olindi!")


def mavjud_kitoblar():
    print("\n--- Mavjud kitoblar ---")

    mavjudlar = []
    for kitob in database.books:
        if kitob ['available']:
            mavjudlar.append(kitob)

    utils.royxat_chiqarish(mavjudlar)


def berilgan_kitoblar():
    print("\n--- Berilgan kitoblar ---")

    berilganlar = []
    for kitob in database.books:
        if not kitob ['available']:
            berilganlar.append(kitob)

    utils.royxat_chiqarish(berilganlar)