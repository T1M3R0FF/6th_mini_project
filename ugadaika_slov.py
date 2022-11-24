import random
word_list = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня', 'Кондитер', 'Омар',
             'Пламя', 'Банк', 'Муж', 'Камбала', 'Груз', 'Кино', 'Лаваш', 'Геолог', 'Бальзам', 'Бревно', 'Борец',
             'Самовар', 'Карабин', 'Барак', 'Мотор', 'Шарж', 'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 'Затычка',
             'Ресница', 'Спичка', 'Кабан', 'Синоптик', 'Характер', 'Фундамент', 'Бумажник', 'Библиофил', 'Дрожжи',
             'Казино', 'Конечность', 'Пробор', 'Комбинация', 'Мешковина', 'Процессор', 'Крышка', 'Сфинкс', 'Фунт',
             'Кружево', 'Агитатор', 'Прокол', 'Абзац', 'Караван', 'Леденец', 'Кашпо', 'Вращение', 'Метрдотель',
             'Клавиатура', 'Радиатор', 'Сегмент', 'Обещание', 'Магнитофон']


def get_word():
    a = random.choice(word_list)
    return a.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''']
    return stages[tries]


def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    display_hangman(tries)
    print(word_completion)
    while True:
        word_input = input('Введите букву или слово\n').upper()
        if not word_input.isalpha:
            print('Вы ошиблись, попробуйте еще')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('Уже было')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Вы угадали, поздравляем!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print('Неверный ответ, осталось попыток:', tries)
                print(display_hangman(tries))
                print_word(word, guessed_letters)
                if tries == 0:
                    print('Вы проиграли!')
                    print('Загаданное слово:', word)
                    break
                continue
        if word_input in word:
            guessed_letters.append(word_input)
            for i in word:
                if i not in guessed_letters:
                    print('Верно, продолжайте')
                    print_word(word, guessed_letters)
                    break
                guessed = True
                if guessed:
                    print('Вы выиграли, поздравляем!')
                    print_word(word, guessed_letters)
                    break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print('Неверно, попыток осталось:', tries)
            print(display_hangman(tries))
            print_word(word, guessed_letters)
        if tries == 0:
            print('Вы проиграли!')
            print('Загаданное слово:', word)
            break


play(get_word())



