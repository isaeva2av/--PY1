salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

while True:  # используем цикл с условием
    if months == 0:  # если количество месяцев равно нулю
        break  # то оператор прерывает цикл

    delta = spend - salary  # разница  между расходами и зарплатой, которую также нужно покрыть подушкой безопасности
    months -= 1
    money_capital += delta
    spend *= 1 + increase  # расходы с учетом роста цен

print(round(money_capital))
