import os


class Leofile(object):
    r"""class Leofile make files as object ^_^.
    usage:
        path = '/etc'
        etcObj = Leofile(path)
        nginxConfObj = etcObj.nginx['nginx.conf'].open('r')
        nginxConfObj.read()
    """

    def __init__(self, path, **kwargs):
        self.path = path

    def list(self):
        '''
        return listdir
        '''
        return os.listdir(self.path)

    def __getattr__(self, attr):
        return Leofile(os.path.join(self.path, attr))

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def open(self, mode):
        '''
        return opened file
        '''
        return open(self.path, mode)

    @property
    def isdir(self):
        return os.path.isdir(self.path)

    @property
    def isfile(self):
        return os.path.isfile(self.path)

    @property
    def parrent(self):
        return Leofile(os.path.join(self.path, '..'))

    @property
    def stat(self):
        return os.stat(self.path)
