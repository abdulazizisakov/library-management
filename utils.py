import database


def matn_olish(matn):
    while True:
        val = input(matn).strip()
        if val:
            return val
        print("Bo'sh kiritish mumkin emas!")


def son_olish(matn):
    while True:
        val = input(matn).strip()
        if val.isdigit():
            return int(val)
        print("Faqat butun son kiriting!")


def kitob_topish(kitob_id):
    for k in database.books:
        if k["id"] == kitob_id:
            return k
    return None


def kitob_chiqarish(k):
    h = "Mavjud" if k["available"] else "Berilgan"
    print(f"ID: {k['id']} | Nomi: {k['title']} | Muallif: {k['author']} | Yili: {k['year']} | Holati: {h}")


def royxat_chiqarish(royxat):
    if not royxat:
        print("Kitob topilmadi.")
        return
    print("-" * 50)
    for k in royxat:
        kitob_chiqarish(k)
    print("-" * 50)