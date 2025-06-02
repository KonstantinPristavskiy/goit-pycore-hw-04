import pathlib
# файл з котами має бути в папці модулю
current_dir = pathlib.Path(__file__).parent


def get_cats_info(path):
    try:
        # відкриваємо файл з зарплатами
        with open(current_dir/ path, encoding="UTF-8") as cats_file:
            
            # зчитуємо рядки
            lines = cats_file.readlines()

            # if lines are empty, file is emply, return None
            if not lines:
                print("Файл порожній")
                return None
            
            # створюємо список з данними кожного кота
            cats_list = [line.strip().split(",") for line in lines]
            
            try:
                # створюємо список словників з правильними даними
                cats_list_of_dicts = [{"id": cat[0], "name": cat[1], "age": int(cat[2])} for cat in cats_list]
            except (IndexError, ValueError) as e:
                print(f"Помилка в форматі даних: {e}")
                return None 
            
            return cats_list_of_dicts

    except FileNotFoundError:
        print("Файл не існує")
        raise FileNotFoundError
    except Exception as e:
        print(f"Помилка при роботі з файлом: {e}")
        return None
    





if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)

    