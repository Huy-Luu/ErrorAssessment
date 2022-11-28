class FileReader():
    @staticmethod
    def readFromText(path):
        file = open(path, "r")
        data = []
        for line in file:
            data.append(line.rstrip())
        return data