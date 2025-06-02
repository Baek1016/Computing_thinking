#2~9까지의 구구단을 중첩 반복문을 이용하여 해결사시오.

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j:2d}")
    print()  # 각 단 사이에 빈 줄 추가