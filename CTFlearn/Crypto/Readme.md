# Crypto
## Có những bài cơ bản mình để ở trong file Crypto.docx
### *Defying Hell*
- Bài này là một cách viết chơi chữ. Nhìn vào tên và đọc bài thì chắc đây là Diffie Hellman
- Với các dữ hiện đã cho:
```
p: 0x8c5378994ef1b
g: 0x02

A: 0x269beb3b0e968
B: 0x4757336da6f70
```
- Đề bài yêu cầu tìm a và b là hai khóa bí mật mà Alice và Bob chọn ngẫu nhiên cho mình. Để tìm giải quyết bài này ta phải bắt buộc giải bài toán logarit rời rạc. a^x = y, a = logay.

- Thật may sao khi ta trừ p cho 1 thì được một số gọi là smooth number (wiki search nha) ta có thể áp dụng thuật toán pohlig-hellman. ( Ta nên vào wiki đọc thiệt kỹ là nắm bắt cho chắc thuật toán này để giải quyết cho dễ). Dưới đây là trang web giúp ta tìm được hai số a,b ta cần tìm. Nên nhớ nắm vững và đủ kiến thức trước khi dùng nó.

- https://case.edu/artsci/math/singer/Sage3/pohlig-hellman.html

  - Kết quả của a và b
  
```
a= 48336C6C30
b= 467231336E64
```
Theo đề bài thì decode rồi submit nhé!

Flag is: CTFlearn{H3ll0_Fr13nd}

### The Most Secured Crypto-Channel
- Bài này nói về sự trao đổi khóa sử dụng thuật toán BB84. Ta cần nắm rõ thuật toán này để làm bài. 
- Quá trình trao đổi khóa giữa Alice và Bob
1. Alice sẽ chọn ngẫu nhiên các photon theo cả hệ đo phân cực thẳng và hệ đo phân cực chéo. 
2. Alice ghi lại các trạng thái của các photon rồi gửi cho Bob. 
3. Bob nhận các photon và đo trạng thái phân cực một cách ngẫu nhiên theo hệ đo phân cực thẳng hoặc hệ đo phân cực chéo. Bob ghi lại hệ ño sử dụng hệ đo phân cực và kết quả các phép đo phân cực. Chú ý là kết quả này có thể khác kết quả của Alice nếu như hai người không sử dụng hệ đo giống nhau. 
4. Bob thông báo cho Alice biết các hệ đo phân cực mà mình đã sử dụng, nhưng không thông báo kết quả các phép đo. 
5. Alice thông báo cho Bob biết hệ đo nào là ñúng. (Hệ đo đúng là hệ đo mà Alice và Bob cùng sử dụng để đo phân cực). 
6. Alice và Bob sẽ loại bỏ các dữ liệu từ các phép đo không đúng. Các dữ liệu từ phép đo đúng sẽ được chuyển thành chuỗi các bít, theo các quy ước sau:
```
Chéo trái  : 1 , chéo phải  : 0.
Thẳng ngang  : 1, thẳng đứng: 0. 
```

![image](https://user-images.githubusercontent.com/59040797/93910172-eaebd800-fd2a-11ea-921f-49969af0695c.png)

Chúng ta có 3 file transmission chứa thông tin qua lại giữa việc trong đổi khóa. Ta phải dựa vào nó để tìm ra khóa và giải quyết bài thi
1. Alice gửi trạng thái của các photon cho Bob. Chúng ta có hai dạng ( '-'or'|' hay '\' or '/' )
2. Máy đo của Bob có 2 dạng 'x' and '+'
3. Alice gửi đánh giấu nơi đúng cho Bob 'v'
``` python
def get_agreed_bytes(data_sent, bases_measured, bases_correct):
    agreed_bits = []
    i=0
    for i in range(len(str(bases_correct))):
        if bases_correct[i] == 'v':
            if bases_measured[i] == '+':
                if data_sent[i] == '-':
                    agreed_bits.append(0)
                else:
                    agreed_bits.append(1)
            else:
                if data_sent[i] == '/':
                    agreed_bits.append(0)
                else:
                    agreed_bits.append(1)
    return ''.join([str(c) for c in agreed_bits]) 
```
Tại ta không biết ý đồ của tác giả nên '-'= 1 or 0, '/'= 1 or 0. Nên trường hợp này ta chịu phải thử 4 trường hợp.

Flag is: CTFlearn{Qu4n7umCryp70gr4phyIs4Fu7ur3}

### Skynet Is (Almost) Taking Over

Ngay đầu bài tác giả cho biết các số nguyên tố họ cung cấp sẽ có liên quan GCD với nhau "using a very small list of primes for RSA style encryption purposes". Do đó ta tìm GCD giữa 3 số thì sẽ tìm được số p và q. 

``` python
def gcd(a, b) : 
      
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a)
```
- Đoạn code trên giúp ta tìm đươc ước chung lớn nhất và đó chính là p ta cần tìm. Sau khi tìm được p thì q cũng dễ dàng tìm được (q = n/p)
- Ta đã có p,q,e,c và đi tới bước cuối cùng là tìm d.
``` python
def Modulo_Inverse(e,o):
    y0 = 0
    y1 = 1
    phi = o
    d=0
    while e > 0:
        r = o % e
        if r==0:
            r=0
            break
        q = o // e
        d = y0-y1*q
        o=e; e=r; y0=y1; y1=d
    if(d<0):
        d=phi+d
    return d
```
- Đoạn code trên áp dụng thuật toán Euclid mở rộng để tìm d (search wiki là sẽ có làm làm theo các bước để hoàn thành code nhé!)
- Tiếp theo là giải mã D = C^d mod n.
- Lưu ý: khi chúng ta giải mã ra được một dãi số thì phải convert sang hex rồi sang ascii nhé

Flag is: CTFlearn{will_he_be_back}
