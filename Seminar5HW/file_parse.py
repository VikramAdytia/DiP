import os


def parse_path(path):
    filepath, file_extension = os.path.splitext(path)
    dirname= os.path.dirname(path)
    filename = os.path.basename(filepath)
    return dirname, filename, file_extension


print(parse_path(r"C:\Users\USER\IdeaProjects\DiP\Seminar5HW\file_parse.py"))
