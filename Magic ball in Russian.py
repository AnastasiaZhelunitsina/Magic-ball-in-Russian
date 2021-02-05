from random import choice
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Я магический шар, и я знаю ответ на любой твой вопрос.')
print()
name = input('Пожалуйста, ведите своё имя: ')
print(f'Здравствуйте, {name}! Добро пожаловать!')
print(f'{name}, если Вы хотите задать мне вопрос - введите "Да", если хотите выйти введите- "Выход"')
decision = input().lower()
if decision == 'y' or decision == 'yes' or decision == 'yep' or decision == 'да' or decision == 'д' or decision == 'ага' or decision == 'угу' or decision == 'ад'or decision == 'lf':
    print('Замечательно! Тогда начнём!')
elif decision == 'no' or decision == 'выход' or decision == 'выйти' or decision == 'нет' or decision == 'неа' or decision == 'н':
    print('Очень жаль. Был рад Вас видеть! Когда появятся вопросы обязательно возращайтесь')
    exit()
question = input('Пожалуйста, введите свой вопрос: ')
print()
print(choice(answers))
while True:
    print()
    again = input('Хотите ли Вы задать ещё вопрос? Если хотите продолжить - введите "Да", если хотите выйти введите- "Выход"').lower()
    if again == 'y' or again == 'yes' or again == 'yep' or again == 'да' or again == 'д' or again == 'ага' or again == 'угу' or again == 'ад' or again == 'lf':
        print('Отлично!')
        question = input('Пожалуйста, введите свой вопрос: ')
        print()
        print(choice(answers))
        print()
    elif again == 'no' or again == 'выход' or again == 'выйти' or again == 'нет' or again == 'неа' or again == 'н' or again == 'в':
        print('Возвращайтесь если возникнут вопросы!')
        break