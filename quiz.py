print("Добро пожаловать в квиз по стартапам!")
print("Ответь на следующие вопросы: ")

question =[
  '1.Как называется компания, которая создается для развития новой идеи или инновационного продукта?',
   '2.Как называется человек или компания которая вкладывает деньги в бизнес с целью получения прибыли?',
  "3. Как называется капитал, который дают инвесторы на развитие стартапа?", 
  "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?", 
  "5. Какой план создают перед тем, как открывать стартап и занимать деньги?", 
  "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?", 
  "7. Как называется разница между выручкой и затратами компании?",
  '8'
]

answers = [
  'стартап', 
  'инвестор',
  "Инвестиция",
  "MVP", 
  "Бизнес-план",
  "Конкуренты",
  "Прибыль"
]

score = 0
print(question[0])

user_input = input("введите ответ:")
if answers[0].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

print(question[1])

user_input = input("введите ответ:")
if answers[1].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")


print(question[2])

user_input = input("введите ответ:")
if answers[2].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

print(question[3])

user_input = input("введите ответ:")
if answers[3].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

print(question[4])

user_input = input("введите ответ:")
if answers[4].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

print(question[5])

user_input = input("введите ответ:")
if answers[5].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

print(question[6])

user_input = input("введите ответ:")
if answers[6].lower() == user_input.lower():
  print("правильно")
  score += 1
else: 
  print ("неправильно")

#print(f'ваш результа {score} из {len(question)}')

if score == 6 or score == 7:
  print("Это отличный результат! Ты много знаешь о стартапах.")
elif score == 3 or score == 4 or score == 5:
  print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о стартапах")
elif score == 0 or score == 1 or score == 2:
  print("Видимо, ты только начинаешь свой путь к стартапам! Ты ещё много чего узнаешь о мире, где мы живём")