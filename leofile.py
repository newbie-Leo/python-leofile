import os


class Leofile(object):
    r"""class Leofile make files as object ^_^.
    usage:
        path = '/etc'
        etc = Leofile(path)
        nginx_config = etc.nginx['nginx.conf'].open('r')
        nginx_config.read()
    """

    def __init__(self, path, **kwargs):
        self.path = path

    def __str__(self):
        return "Leofile of %s" % self.path

    def __iter__(self):
        return iter(self.list())

    def __repr__(self):
        return "<%s>" % self.__str__()

    def list(self):
        '''
        return listdir
        '''
        return [Leofile(os.path.abspath(i)) for i in os.listdir(self.path)]

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
        return Leofile(os.path.abspath(os.path.join(self.path, '..')))

    @property
    def stat(self):
        return os.stat(self.path)
