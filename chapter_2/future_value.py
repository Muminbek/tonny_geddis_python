# Получить требуемое будущее значение.
future_value = float(input('Bвeдитe требуемое будущее значение: '))

 # Получить годовую процентную ставку.
rate = float(input('Bвeдитe годовую процентную ставку: '))

 # Получить количество лет роста стоимости денег.
years = int(input('Bвeдитe количество лет роста стоимости денег: '))

# Рассчитать сумму, необходимую для внесения на счет.
present_value = future_value / (1.0 + rate)**years

# Показать сумму, необходимую для внесения на счет.
print('Baм потребуется внести сумму: ', present_value)