#tasadofi_library_pyton

def integerlist(n, a, b): # تولید لیست عدد تصادفی
    import math
    seed, s, l = int(8659836740), [], n
    while n > 0:
        seed = seed + math.sqrt(seed)
        random_number = ((seed * 1603515254 + 12345) % 32768) % (b - a + 1) + a
        s.append(int(random_number))
        seed += math.sqrt(seed)
        n -= 1
    return s





def floatlist(n, a, b): # تولید لیست اعداد اعشاری
    import math
    k, b, s = str(b), int(b), []
    seed = int(8659836740)
    while n > 0:
        seed = seed + math.sqrt(seed)
        random_number = ((seed * 1603515254 + 12345) % 32768) % (b - a + 1) + a
        random_number_float = ((seed * 3729749224 + 999398) % 71506) % (b - a + 1) + a
        s.append(random_number+random_number_float/10**len(k)+1)
        seed += math.sqrt(seed)
        n -= 1
    return s





def normal(m, s):
    import math
    seed = math.sqrt(m/s)
    u1 = ((seed * 1603517254 + 12345) % 32768) % (m - s + 1) + s
    u2 = ((seed * 9013519867 + 47898) % 12008) % (m - s + 1) + s
    u1, u2 = u1/len(str(u1)), u2/len(str(u2))
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    x = z0 * s + m
    return x





def repinteger(a, b):
    import math
    import time
    seed = int(time.time())
    seed = seed + math.sqrt(seed + a * b)
    random_number = ((seed * 5503908254 + 76635) % 30937) % (b - a + 1) + a
    x = int(random_number)
    return x






def float(a, b):
    import math
    k, b= str(b), int(b)
    seed = int(9384836740)
    seed = seed + math.sqrt(seed+a**b)
    random_number = ((seed * 2783515252 + 10045) % 909768) % (b - a + 1) + a
    random_number_float = ((seed * 3700049224 + 939768) % 74506) % (b - a + 1) + a
    x = random_number+random_number_float/10**len(k)+1
    return x




def integer(a, b):
    import math
    seed= int(8659838764)
    seed = seed + math.sqrt(seed+a/b)
    random_number = ((seed * 9903515254 + 77235) % 30768) % (b - a + 1) + a
    x = int(random_number)
    return x

