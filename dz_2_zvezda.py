questions = ['My name ___  Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
count = 0
questions = ['My name ___  Vova', 'I ___ a coder', 'I live ___ Moscow']
answers = ['is', 'am', 'in']
points = []
count = 0
points_total = 0
print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать')
greetings = input().lower()

if greetings == "ready":
    for question in range(len(questions)):
        print(questions[question])
        answer = input()
        if answer == answers[question]:
            print('Ответ верный!')
            count += 1
            point = 3
            points.append(point)
            print()
        else:
            point = 3
            while point >= 1:
                if answer == answers[question]:
                    print('Ответ верный!')
                    count += 1
                    points.append(point)
                    break
                elif answer != answers[question] and point == 1:
                    print(f'Увы, но нет. Верный ответ: {answers[question]}')
                    break
                else:
                    print(f'Осталось попыток: {point - 1}, попробуйте еще раз!')
                    answer = input()
                    point -= 1
                    continue
            print()

    for i in points:  # подсчёт суммы баллов
        points_total += i

    if points_total == 1:  # корректные окончания для процентов
        ending_point = 'балл'
    elif 2 <= points_total <= 4:
        ending_point = 'балла'
    else:
        ending_point = 'баллов'

    last_ending = count % 10  # корректные окончания для вопросов
    if last_ending == 1:
        ending_question = 'вопрос'
    elif 2 <= last_ending <= 4:
        ending_question = 'вопроса'
    else:
        ending_question = 'вопросов'

    print(
        f'Вот и все! Вы ответили на {count} {ending_question} из {len(questions)} верно, Вы набрали {points_total}, {ending_point}.')

else:
    print('Кажется, вы не хотите играть. Очень жаль.')
