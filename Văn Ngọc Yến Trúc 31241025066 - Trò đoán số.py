import random

tien = 100
x = 5
win = 0
lose = 0

while tien >= x:
    comp_number = random.randint(1, 100)
    while True:
        if tien < x:
            print("💸 Bạn đã hết tiền!")
            break

        guess = int(input("Bạn đoán số: "))

        if guess == comp_number:
            win += 1
            tien += 10
            print(" Correct! Bạn đã đoán đúng!")
            print(f"Số tiền hiện tại: ${tien}")
            break
        elif guess < comp_number:
            lose += 1
            tien -= x
            print("Quá nhỏ")
            print(f"Số tiền còn lại: ${tien}")
        else:
            lose += 1
            tien -= x
            print("Quá lớn")
            print(f"Số tiền còn lại: ${tien}")

    if tien >= x:
        cont = input("Bạn có muốn chơi tiếp không (y/n)? ").lower()
        if cont != "y":
            break
    else:
        break

print(f"Tổng số lần thắng: {win}")
print(f"Tổng số lần thua: {lose}")
print(f"Số tiền cuối cùng: ${tien}")




