import csv
import Multilist


class Files():
    def read_file(self, path):
        with open(path, encoding="utf-8-sig") as file:
            
            reader = csv.DictReader(file)

            for row in file:
                