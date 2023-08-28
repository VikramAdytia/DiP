import argparse
from collections import namedtuple
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, filename="task6_log.log", encoding="utf-8", filemode="w")

logger = logging.getLogger(__name__)

File = namedtuple('File', 'name , extension, is_dir, parent_dir')


def parser():
    parser = argparse.ArgumentParser(prog='get_data'
                                     , description='Get data form string'
                                     , epilog='get_data(foobar)')
    parser.add_argument('-p' , '--path', default=r'C:\User', help='path for your heart')
    args = parser.parse_args()
    return read_dir(f'{args.path}')


def read_dir(path: Path):
    for file in path.iterdir():
        foo ='foo'
        bar = 'bar'
        f = File(file.stem if file.is_file() else file.name, file.suffix, file.is_dir(), file.parent)
        logger.info(f)
        if f.is_dir:
            read_dir(Path(f"{f.parent_dir}\\{f.name}"))



if __name__ == '__main__':
    print(read_dir(Path(r'C:\Users\USER\IdeaProjects\DiP\sem15')))

