import os
import sys
from functools import total_ordering


@total_ordering
class File:
    def __init__(self, path, name, size):
        self.size = size
        self.name = name
        self.path = path

    def __str__(self) -> str:
        return 'File: {}\{} with size: {} kb'.format(self.path, self.name,
                                                     '%.2f' % self.size)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, File):
            return False
        return self.name == o.name and self.size == o.size

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        return self.name < other.name


def load_folder_content(foldername) -> list:
    files = []
    for (dirpath, dirnames, filenames) in os.walk(foldername):
        for (filename) in filenames:
            size = os.path.getsize(dirpath + "//" + filename) / 1024
            fn = File(dirpath, filename, size)
            files.append(fn)
    files.sort()
    return files


def remove_unique_files(files) -> list:
    return [file for file in files if files.count(file) > 1]


if __name__ == '__main__':
    folder_content = load_folder_content(sys.argv[1])
    files = remove_unique_files(folder_content)
    if len(files) == 0:
        print("No duplicate files found")
    else:
        print("Following duplicates found:")
        print(*files, sep='\n')
