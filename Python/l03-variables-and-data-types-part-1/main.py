# Завдання:
# Напиши програму, яка обчислює вартість покупки з урахуванням знижки.

# Користувач вводить початкову вартість товару (у гривнях).
price = float(input("Enter price: "))

# Користувач вводить відсоток знижки (наприклад, 10 для 10%).

percents = float(input('Enter discount: '))

# Програма повинна обчислити:
# Розмір знижки в гривнях.

discount = (price / 100) * percents

# Кінцеву вартість товару після знижки.

final_price = price - discount

# Виведи результати у зрозумілому вигляді.
print('Discount:', discount, 'грн')
print('Final price:', final_price, 'грн')
