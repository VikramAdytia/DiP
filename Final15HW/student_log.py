import argparse
import logging
from student_exeptions import StudentNameError, InvalidSubjectError, InvalidScoreError
from student import Student

logging.basicConfig(filename='student_log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s'
                    , encoding="utf-8", filemode="a")


def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        #name, csv_filename ="5John", "subjects.csv"

        student = Student(args.name, args.csv_filename)
        #student = Student(name, csv_filename)

        # Вызываем ошибку класса Student 
        student.add_score("Matth", 6)

    except StudentNameError as e:
        logging.error(f'Invalid student name format: {args.name} {e}')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e}')

if __name__ == '__main__':
    main()


# python student_log.py John subjects.csv - запуск из командной строки
# python student_log.py 7John subjects.csv - запуск из командной строки  ошибкой формата имени
# Здесь student_log.py - имя файла со скриптом, John - имя студента, subjects.csv - имя CSV-файла с предметами."""