class Files():
    def read_file(self, path):
        with open(path, "r") as file:
            line1 = file.readline()
            print(line1.strip())