# Programming

### **The Credit Card Fraudster**

- Đọc đề bài ta nắm được hai ý chính: 
  - Card number multiple of 123457
  - Luhn check digit is valid

**Phải nắm được thuật toán luhn mới làm được bài này nhé**
> Card Number: 543210******1234
> Như vậy còn thiếu 6 số. Ta bruce force để điền vào số còn trống.
- Ý tưởng:
  - Thay * thành 0
  - Cho i chạy [0,999999]
  - Card number = Card number + i*100000 
``` python
Card_Number = 5432100000001234
arr_Step  = [] # Mảng chứ số có khả năng là đáp án
i=0
for i in range(999999):
    i=i+1
    Test = Card_Number + i*10000
    if Test %123457 == 0:
        print(Test)
        continue 
```
làm tới đây thôi thì ra kết quả rồi nhé, cứ thử những đáp án sẽ có một đáp án chúng

Nhưng với tinh thần thép của programmer thì kho cho bạn làm điều đó. 

Tiếp với với thuật toán Luhn. 

``` python
def Check_Luhn_Valid(number):
    i=0
    odd = 0
    feven = 0
    for i in range(16):
        if i%2==0:
            step = int(str(number)[i])*2 
            if step >= 10:           # nếu >=10 thì chia ra cộng 2 số. VD 12 => 1+2
                odd=odd + int(str(step)[0]) + int(str(step)[1])
            else :
                odd = odd + step
        else :
            feven = feven + int(str(number)[i])

    if (odd + feven) % 10 == 0:
        return True
    else:
        return False
```

Flag is: CTFlearn{5432103279251234}

