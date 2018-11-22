# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке. Для решения
# задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()


def substring_count(s):
    len_s = len(s)
    subs_collection = set()
    len_sub = 1
    while len_sub < len_s:
        for i in range(len_s):
            if i+len_sub <= len_s:
                subs_collection.add(hash(s[i:i+len_sub]))
        len_sub += 1
    return len(subs_collection)


print(substring_count("Абсолютно любая строка"))
