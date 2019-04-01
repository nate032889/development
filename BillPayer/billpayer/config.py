import os


class Basic:

    pass


class Production(Basic):

    def __init__(self):
        super(Basic, self).__init__()
        pass


class Development(Basic):

    def __init__(self):
        super(Basic, self).__init__()
        pass


config = {"default": Development, "production": Production}