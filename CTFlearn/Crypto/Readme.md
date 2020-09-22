# Crypto
- Bài giải ở trong file Crypto.docx
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
