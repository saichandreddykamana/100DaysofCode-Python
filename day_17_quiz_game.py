import random

class Data:
  questions = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer


class Quiz:
  def __init__(self, list):
    self.list = list
    self.question_number = 0
    self.questions_asked = 0
    self.score = 0

  def next(self):
    self.question_number = random.randint(0, len(self.list) - 1)
    current_question = self.list[self.question_number]
    user_answer = input(f' Question : {self.questions_asked + 1}  --> {current_question.text} (True/False) :  ')  
    self.list.remove(self.list[self.question_number])
    self.questions_asked += 1
    self.check_user_answer(user_answer, current_question.answer)

  def still_questions_exists(self):
    if len(self.list) > 0:
      return True
    return False

  def check_user_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      self.score += 1
      print("You're answer is right.")
    else:
      print("You're answer is wrong.")
    print(f'The correct answer is {correct_answer}.')
    print(f' Your score is : {self.score} / {self.questions_asked}')

questions = []
for question in Data.questions:
  new_question = Question(question['text'], question['answer'])
  questions.append(new_question)

quiz = Quiz(questions)
while quiz.still_questions_exists():
  print("--" * 40)
  quiz.next()

print('Game Over!!!!')
print(f'Your final Score : {quiz.score} / {quiz.questions_asked}')
