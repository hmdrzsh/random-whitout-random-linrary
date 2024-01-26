# تابعی جهت تولید عدد اعشاری تصادفی یکنواخت در بازه a تا b

def random_number_flt(n, a, b): # تولید تابع
    import math
    k, b, s = str(b), int(b), []
    seed = int(8659836740) # ایجاد سید ثابت
    while n > 0: #ایجاد حلقه جهت تولید اعداد تصادفی
        seed = seed + math.sqrt(seed) # تغییر سیید
        random_number = ((seed * 1603515254 + 12345) % 32768) % (b - a + 1) + a # تولید عدد تصادفی صحیح
        random_number_float = ((seed * 3729749224 + 999398) % 71506) % (b - a + 1) + a # تولید عدد تصادفی اعشاری
        s.append(random_number+random_number_float/10**len(k)+1) # اضافه کردن به لیست
        seed += math.sqrt(seed) #تغییر مجدد سید
        n -= 1
    return s

print(*random_number_flt(33, 0, 800))
