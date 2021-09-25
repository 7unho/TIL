# 설탕을 정확하게 N킬로그램 배달
# 봉지는 3키로, 5키로
# 배달할 수 없다면 -1 출력

input_N = int(input())
five_kg, three_kg = 0, 0

if input_N % 5 == 0:
    five_kg = input_N // 5
else:
    for i in range(1, (input_N // 3) + 1) :
        if(input_N - (i * 3)) % 5 == 0:
            three_kg += i
            five_kg += int(input_N - (i * 3) / 5)
            break

print("-1" if five_kg == 0 and three_kg == 0 else five_kg + three_kg)

