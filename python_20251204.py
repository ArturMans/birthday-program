# Файл: birthday_program.py

import datetime

# Шаблоны цифр для электронного табло (7x5)
digit_patterns = {
    '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
    '1': ['  *  ', ' **  ', '  *  ', '  *  ', ' *** '],
    '2': [' *** ', '*   *', '   * ', '  *  ', '*****'],
    '3': [' *** ', '    *', '  ** ', '    *', ' *** '],
    '4': ['*   *', '*   *', '*****', '    *', '    *'],
    '5': ['*****', '*    ', '**** ', '    *', '**** '],
    '6': [' *** ', '*    ', '**** ', '*   *', ' *** '],
    '7': ['*****', '    *', '   * ', '  *  ', ' *   '],
    '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
    '9': [' *** ', '*   *', ' ****', '    *', ' *** '],
    ' ': ['     ', '     ', '     ', '     ', '     ']
}

def get_weekday(date_obj):
    """Определяет день недели для даты"""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", 
            "Пятница", "Суббота", "Воскресенье"]
    return days[date_obj.weekday()]

def is_leap_year(year):
    """Проверяет, является ли год високосным"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    """Вычисляет возраст пользователя"""
    today = datetime.date.today()
    age = today.year - birth_date.year
    
    # Проверяем, был ли уже день рождения в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def print_digital_date(date_str):
    """Выводит дату в формате электронного табло"""
    # Разделяем дату на отдельные символы
    chars = list(date_str.replace(' ', ''))
    
    # Добавляем пробелы между числами
    formatted_chars = []
    for i, char in enumerate(chars):
        formatted_chars.append(char)
        if i < len(chars) - 1 and (i + 1) % 2 == 0:
            formatted_chars.append(' ')
    
    # Выводим построчно
    for row in range(5):
        line = ""
        for char in formatted_chars:
            if char in digit_patterns:
                line += digit_patterns[char][row] + "  "
            else:
                line += "     " + "  "
        print(line)

def main():
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ РАБОТЫ С ДАТОЙ РОЖДЕНИЯ")
    print("=" * 50)
    
    try:
        # Ввод данных
        day = int(input("Введите день рождения: "))
        month = int(input("Введите месяц рождения: "))
        year = int(input("Введите год рождения: "))
        
        # Создаем объект даты
        birth_date = datetime.date(year, month, day)
        
        # 1. Выводим введенную дату
        print(f"\nДата рождения: {birth_date.strftime('%d.%m.%Y')}")
        
        # 2. Определяем день недели
        weekday = get_weekday(birth_date)
        print(f"Это был: {weekday}")
        
        # 3. Проверяем високосный ли год
        leap_status = "високосный" if is_leap_year(year) else "не високосный"
        print(f"Год {year} - {leap_status}")
        
        # 4. Вычисляем возраст
        age = calculate_age(birth_date)
        print(f"Сейчас вам: {age} лет")
        
        # 5. Выводим дату в формате электронного табло
        print(f"\nДата рождения в формате электронного табло:")
        print_digital_date(birth_date.strftime('%d %m %Y'))
        
        # Дополнительная информация
        print(f"\n{'=' * 50}")
        print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ:")
        print(f"Дней с рождения: {(datetime.date.today() - birth_date).days}")
        print(f"Знак зодиака: {'[можно добавить расчет]'}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
        print("Пожалуйста, введите корректные данные!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()