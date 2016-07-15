import os


class Leofile(object):

    def __init__(self, path, **kwargs):
        self.path = path

    def list(self):
        return os.listdir(self.path)

    def __getattr__(self, attr):
        return Leofile(os.path.join(self.path, attr))

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def open(self, mode):
        return open(self.path, mode)
