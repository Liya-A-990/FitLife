# Проект FitLife - MVP версия 1.0
# Начальное приветствие пользователя программой
print('Добро пожаловать в FitLife MVP!')
print('Для начала давайте познакомимся.')

# Пользователь вводит имя и возраст, возраст преобразовываем в целое число
user_name = input('Как вас зовут?\n').strip().title()

try:
    user_age = int(input('Сколько вам лет?\n'))
    
except ValueError: # Если пользователь введет что-то не то
    user_age = input('Упс! Ошибка! Пожалуйста, введите ваш возраст\n').strip()
    user_age = int(user_age)         
    
# Пользователь вводит вес и рост, преобразовываем их в числа с плавающей точкой
# Используем конструкцию try-except для обработки потенциальных ошибок
try:
    user_weight = input('Напишите ваш вес (например, 50.5)\n')
    user_weight = float(user_weight)
    
except ValueError:
    user_weight = input('Пожалуйста, введите вес, используя точку\n')
    user_weight = float(user_weight)
    
try:
    user_height = input('И рост в метрах (например 1.75)\n')
    user_height = float(user_height)
    
except ValueError:
    user_height = input('Пожалуйста, введите рост в метрах, используя точку\n')
    user_height = float(user_height)

print()
print('Ваше имя -', user_name)
print('Ваш возраст - ', user_age)
print(f'Ваш вес - {user_weight} кг')
print(f'Ваш рост - {user_height} м')

# Рассчитываем ИМТ и округляем его до одного знака после точки
bmi = user_weight / (user_height ** 2) 
bmi = round(bmi, 2)

# Используем константы
# Стандартная рекомендация для поддержания водного баланса - 30 мл/кг
water_reg_kg = 30 
# Кол-во мл в литрах - тоже постоянная величина
ml_in_l = 1000

# Рассчитываем норму воды в миллилитрах, переводим в литры,
# округляем до двух знаков после запятой
water_ml = user_weight * water_reg_kg 
water_l = water_ml / ml_in_l
water_l = round(water_l, 1)

# Программа выводит аккуратный отчет на экран с помощью f строк
print()
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} в день')
print()
print('Расчет окончен. Будьте здоровы!')
