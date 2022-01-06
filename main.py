from src.book import parse_book
from src.picker import QuestionSelector
from pathlib import Path

BOOK_PATH = Path('books\linear_algebra.yaml')
NUM_QUESTIONS = 10

def main():
    #parse book
    book = parse_book(BOOK_PATH)
    picker = QuestionSelector(book, NUM_QUESTIONS)
    return picker(NUM_QUESTIONS)

if __name__ == "__main__":
    main()