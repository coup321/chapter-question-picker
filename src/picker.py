from typing import Union
from pathlib import Path
import random

class QuestionSelector:
  """
  Selects 'n' random questions from 'chapters' with 'chapter_question_count'
  Attr:
    chapter_dict : dict {str:int}

  Methods:
    select_n_questions(n:int) -> dict {chapters Union[str, int] : questions : list}
  """
  def __init__(self, book, num_questions):
    self.book = book
    self.num_questions = num_questions
    self.selection = None

  def get_questions(self):
    section_list = [chapter.sections for chapter in self.book.chapters]
    return [item for sublist in section_list for item in sublist] #this comprehension flattens section_list

  def select_questions(self, n : int) -> dict:
    questions = self.get_questions()
    if not questions:
      raise ValueError('chapter_dict is empty')

    picked_questions = []
    for question in range(n):
      random_section = random.choice(list(self.chapter_dict.keys()))
      random_question = random.randint(1,self.chapter_dict[random_section])
      
      if random_section in picked_questions.keys():
        picked_questions[random_section] += [random_question]
      else:
        picked_questions[random_section] = [random_question]

    self.selection = picked_questions
    return picked_questions

  def print_selection(self):
    if not self.selection:
      raise Exception('No questions election has been made')
    output = ''
    for key, value in self.selection.items():
      output += f'Chapter: {key} Questions: ' + ', '.join([str(x) for x in value]) + '\n'
    return output
    

  def new_chapter(self, dict):
    #should add a new chapter to the yaml
    pass

  def total_questions(self):
    questions = self.get_questions()
    return sum([list(q.values())[0] for q in questions])

  def __call__(self, n):
    if n > self.total_questions():
      raise ValueError("""number of questions requested is greater than number
                        of questions in question dictionary""")
    return self.select_questions(n)  

  def __repr__(self):
    output = ''
    for key, value in self.get_questions():
      output += f'Chapter: {key} Number of questions: {value}\n'
    return output
    