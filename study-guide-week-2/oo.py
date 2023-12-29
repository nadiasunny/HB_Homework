# Create your classes here
class Student():
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question():
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = input(f'{self.question} > ')
        return user_answer == self.correct_answer
        

class Exam():
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
    
    def administer(self):
        correct = 0
        for ques in self.questions:
            if ques.ask_and_evaluate():
                correct+=1

        return (correct/len(self.questions)*100)


class StudentExam(Student, Exam, Question):
    def __init__(self, student, exam):
        self.student = student
        self.questions = []
        self.exam = exam
        self.score = 0

    def take_test(self):
        self.score = self.administer()
        print(self.score)


def example():
    susy = Student('Sussane', 'Bothers', '101 Nubo Dr')
    gummy = Exam('gum?')

    ques = Question('What is you gum?', 'No Gum')
    ques2 = Question('What is you gum?', 'No Gum')
    SusyMidterm = StudentExam(susy, gummy)
    SusyMidterm.add_question(ques)
    SusyMidterm.add_question(ques2)
    SusyMidterm.take_test()

example()


#     ButtExam = Exam('ButtExam')
#     ButtExam.add_question(['Did is hurt?', 'Yes'])
#     ButtExam.add_question(['Will you be comming back?', '*horrified*'])
#     Butina = Student('Butin', 'Amish', "101 Juns Dr")
#     ButEx = StudentExam(Butina, ButtExam, ButtExam.questions)
#     ButEx.administer(ButtExam.questions)

