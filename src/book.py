from ast import parse
from importlib.abc import Loader
import yaml
from dataclasses import dataclass
import numpy as np

@dataclass
class Book:
    chapters: list
    title: str
    num_chapters: int
    total_sections: int

@dataclass
class Chapter:
    name: str
    num_sections: int
    sections: list

@dataclass
class Section:
    name: str or int
    num_questions: int

    
def parse_book(path):
    #get chapters and sections from yaml
    chapters = []
    sections = []
    with open(path) as f:
        doc = yaml.load(f, Loader=yaml.Loader)
    for C in doc['chapters']:
        for section in C['sections']:
            section_name, num_questions = section.popitem()
            sections.append(Section(section_name, num_questions))

        chapters.append(Chapter(C['name'], C['num_sections'], sections))

    book_title = doc['title']
    num_chapters = len(chapters)
    total_sections = sum([len(C.sections) for C in chapters])
    return Book(chapters, book_title, num_chapters, total_sections)

# book = parse_book('books\linear_algebra.yaml')
# print(book.chapters[0].sections[0])

#section_list = [c.sections for c in book.chapters]
# with open('books\linear_algebra.yaml') as f:
#     doc = yaml.load(f, Loader=yaml.Loader)
# print(doc['chapters'][0]['sections'][0].popitem())