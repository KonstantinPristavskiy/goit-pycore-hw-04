import pathlib
# файл з зарплатами має бути в папці модулю
current_dir = pathlib.Path(__file__).parent


def total_salary(path: str) -> tuple | None:
    try:
        # відкриваємо файл з зарплатами
        with open(current_dir/ path, encoding="UTF-8") as salary_file:

            # зчитуємо рядки
            lines = salary_file.readlines()

            # if lines are empty, file is emply, return None
            if not lines:
                print("Файл порожній")
                return None
            

            # створюємо список списків з імʼям та ЗП
            names_salaries_list = [line.strip().split(",") for line in lines]


            try:
                # створюємо список тільки з ЗП
                salaries_list = [int(item[1]) for item in names_salaries_list]
            except (IndexError, ValueError) as e:
                print(f"Помилка в форматі даних: {e}")
                return None
            
            # рахуємо суму всіх ЗП і середню ЗП
            salary_total = sum(salaries_list)
            salaries_average = salary_total/len(salaries_list)
            return salary_total, salaries_average

    # якщо файл не існує
    except FileNotFoundError:
        print("Файл не існує")
        return None
    # будь яка інша помилка при відкритті файлу
    except Exception as e:
        print(f"Помилка при роботі з файлом: {e}")
        return None

    

if __name__ == "__main__":
    # створюємо кортеж результатів
    result = total_salary("salaries.txt")
    # якщо нам пришли дані, виводимо їх, якщо None -- нічого не робимо
    if result is not None:
        total, average = result
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    