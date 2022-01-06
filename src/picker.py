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

  def get_chapters(self) -> list:
    #return book chapters
    return self.book.chapters

  def get_sections(self) -> list:
    #return list of all the questions
    sections = []
    for C in self.book.chapters:
      sections += C.sections
### START HERE
  def select_questions(self, n : int) -> dict:
    questions = self.get_questions()
    if not questions:
      raise ValueError('chapter_dict is empty')

    picked_questions = []
    for question in questions:
      random_section = random.choice([Q.name for Q in questions])
      random_question = random.randint(1, question.num_questions)
      
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
    #should add a new chapter
    pass
  def export_book(self):
    #export book as yaml
    pass

  def total_questions(self):
    return sum([Q.num_questions for Q in self.get_questions()])

  def __call__(self, n):
    if n > self.total_questions():
      raise ValueError("""number of questions requested is greater than number
                        of questions in question dictionary""")
    return self.select_questions(n)  

  def __repr__(self):
    output = ''
    for Q in self.get_questions():
      output += f'Chapter: {Q.name} Number of questions: {Q.num_questions}\n'
    return output
    