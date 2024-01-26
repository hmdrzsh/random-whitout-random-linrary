#تابعی جهت تولید عدد اعشاری تصادفی نرمال با میانگین m و انحراف معیار s

def randomnormal(m, s):
    import math
    seed = math.sqrt(m/s) # ایجاد سید
    u1 = ((seed * 1603517254 + 12345) % 32768) % (m - s + 1) + s # تولید عدد تصادفی 1
    u2 = ((seed * 9013519867 + 47898) % 12008) % (m - s + 1) + s # تولید عدد تصادفی 2
    u1, u2 = u1/len(str(u1)), u2/len(str(u2)) # اعشاری کردن اعداد تصادفی یکنواخت
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2) # ایجاد طبق فرمول
    x = z0 * s + m
    return x

print(randomnormal(m, s))

