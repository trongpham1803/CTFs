def Check_Luhn_Valid(number):
    i=0
    odd = 0
    feven = 0
    for i in range(16):
        if i%2==0:
            step = int(str(number)[i])*2 
            if step >= 10:
                odd=odd + int(str(step)[0]) + int(str(step)[1])
            else :
                odd = odd + step
        else :
            feven = feven + int(str(number)[i])

    if (odd + feven) % 10 == 0:
        return True
    else:
        return False


Card_Number = 5432100000001234
arr_Step  = []
i=0
for i in range(999999):
    i=i+1
    Test = Card_Number + i*10000
    if Test %123457 == 0:
        if Check_Luhn_Valid(Test):
            print(Test)
        continue 