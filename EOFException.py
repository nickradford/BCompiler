class EOFException(Exception):
    def __init__(self):
        Exception.__init__(self, "End of file detected reading source file")