from importlib.abc import Loader
import yaml
from dataclasses import dataclass

with open('books\linear_algebra.yaml') as f:
    doc = yaml.load(f, Loader=yaml.Loader)
    
#print(doc['num_chapters'])
#print(doc['chapters'])
#print(doc['chapters'][0]['sections'])
@dataclass
class Chapter:
    name: str
    num_sections: int
    sections: list
    

def parse_book(path):
    with open(path) as f:
        doc = yaml.load(f, Loader=yaml.Loader)
    chapters = []
    for C in doc['chapters']:
        chapters.append(
            Chapter(C['name'], C['num_sections'], C['sections']))
    return chapters
print(parse_book('books\linear_algebra.yaml')[0])