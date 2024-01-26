import tasadofi

n = 20 #تعداد بازیکن ها
money = n * [25] #پول های تو بازی که از 0 تا 19 برای 20 نفر کد گذاری شدن
i, j = n-1, [] # شمارنده دور بازی

while len(money) > 0:
    person_er = i  # کم کردن یک واحد پول از فرد انتخابگر
    person_en = tasadofi.repinteger(0, i)  # اضافه کردن یک واحد پول به فرد انتخاب شده تصادفی
    i -= 1
    while person_er >= len(money): #این حلقه و حلقه 14 برای کنترل بازیکن های حذف شده است
        person_er = person_er - 1
    money[person_er] -= 1
    while person_en >= len(money):
        person_en -= person_en
    money[person_en] += 1
    print("بازیکن" , person_en+1, "یک واحد پول دریافت کرد!")
    if i == -1: # شرط منفی نشدن تعداد بازیکن ها
        i =19
    if money[person_er] == 0:  # اگر کسی آخرین پولش را بدهد از بازی حذف میشود
        removed_player = money.pop(person_er)
        print("بازیکن شماره ", person_er, "حذف شد!")
        print("در حال شماره بندی مجدد... ")
        print("از شماره بازیکن ها یکی کم شد! ")
        j.append(i)
        if len(money) == 1: # شرط برنده بازی
            print("بازی تمام شد!")
            print(" پول بازیکن برنده: ", *money) # کل پول های ورودی را برمیدارد(500$)
            end = money.pop(0)
