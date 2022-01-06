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
class Question
##### START HERE 1/7
    
def parse_book(path):
    chapters = []
    with open(path) as f:
        doc = yaml.load(f, Loader=yaml.Loader)
    for C in doc['chapters']:
        chapters.append(
            Chapter(C['name'], C['num_sections'], C['sections']))
    book_title = doc['title']
    num_chapters = len(chapters)
    total_sections = sum([len(C.sections) for C in chapters])
    return Book(chapters, book_title, num_chapters, total_sections)

#book = parse_book('books\linear_algebra.yaml')
#section_list = [c.sections for c in book.chapters]
#print([item for sublist in section_list for item in sublist])
#item for sublist in regular_list for item in sublist