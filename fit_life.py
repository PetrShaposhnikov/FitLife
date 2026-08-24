# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
SEPARATE = "*" * 20

# 1. Знакомство
print(SEPARATE)
print("Здравсвтуйте, Вас приветствует программа FitLife.")
print("Давайте рассчитаем Ваш ИМТ и нормы воды в день.")
print(SEPARATE)

user_name = input("Как Вас зовут? ")
user_age = int(input("Сколько Вам лет? "))

# 2. Сбор данных
user_weight = float(input("Какой у Вас вес? "))
user_height = float(input("Какой у Вас рост? "
                          "(введите рост в метрах, используя точку: 1.75)"))

# 3. Логика расчетов, расчет ИМП и нормы воды
bmi = round(user_weight / (user_height ** 2), 1)
water_liters = (user_weight * WATER_PER_KG) / 1000

# 4. Вывод результата
print(SEPARATE)
print(f"Отчет пользователя: {user_name} ({user_age} г.)")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_liters:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
print(SEPARATE)

