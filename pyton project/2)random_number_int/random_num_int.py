# تابعی جهت تولید عدد صحیح تصادفی یکنواخت در بازه a تا b

def random_number_int(n, a, b):# تعربف تابع با 3 متغیر
    import math
    seed, s = int(8659836740), [] # ساخت سید ثابت
    while n > 0: # حلقه جهت ایجاد اعداد تصادفی
        seed = seed + math.sqrt(seed)
        random_number = ((seed * 1603515254 + 12345) % 32768) % (b - a + 1) + a # فرمول اعداد یکنواخت در بازه
        s.append(int(random_number))
        seed += math.sqrt(seed) # تغببر سید
        n -= 1
    return s

print(*random_number_int(1, 7, 99))
