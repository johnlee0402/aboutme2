def calculate_life_number(birthday_str):

    total = 0
    for digit in birthday_str:
        total += int(digit)
    
    return total

x = input("請輸入西元生日 8 位數 (例如 20050101): ")

result = calculate_life_number(x)

print(f"您的第一個數字是: {x[0]}")
print(f"您的西元生日 8 位數相加結果為: {result}")