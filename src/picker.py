import random
from typing import Union
import os

class QuestionSelector:
  """
  Selects 'n' random questions from 'chapters' with 'chapter_question_count'
  Attr:
    chapter_dict : dict {str:int}

  Methods:
    select_n_questions(n:int) -> dict {chapters Union[str, int] : questions : list}
  """
  def __init__(self, chapter_dict):
    self.chapter_dict = chapter_dict
    self.selection = None

  def select_questions(self, n : int) -> dict:
    if not self.chapter_dict:
      raise ValueError('chapter_dict is empty')

    questions = dict()
    for question in range(n):
      random_section = random.choice(list(self.chapter_dict.keys()))
      random_question = random.randint(1,self.chapter_dict[random_section])
      
      if random_section in questions.keys():
        questions[random_section] += [random_question]
      else:
        questions[random_section] = [random_question]
    self.selection = questions
  
    return questions

  def print_selection(self):
    if not self.selection:
      raise Exception('No questions election has been made')
    output = ''
    for key, value in self.selection.items():
      output += f'Chapter: {key} Questions: ' + ', '.join([str(x) for x in value]) + '\n'
    return output
    

  def new_chapter_dict(self, dict):
    self.chapter_dict = dict
  
  def total_chapters(self):
    return len(self.chapter_dict)

  def total_questions(self):
    return sum(self.chapter_dict.values())

  def __call__(self, n):
    if n > self.total_questions():
      raise ValueError("""number of questions requested is greater than number
                        of questions in question dictionary""")
    return self.select_questions(n)  

  def __repr__(self):
    output = ''
    for key, value in self.chapter_dict.items():
      output += f'Chapter: {key} Number of questions: {value}\n'
    return output
    