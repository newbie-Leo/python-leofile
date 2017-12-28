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
        self._path = path

    def __str__(self):
        return "Leofile of %s" % self._path

    def __iter__(self):
        return iter(self.list())

    def __repr__(self):
        return "<%s>" % self.__str__()

    def __getattr__(self, attr):
        return Leofile(os.path.join(self._path, attr))

    def __getitem__(self, attr):
        return self.__getattr__(attr)

    @property
    def isdir(self):
        return os.path.isdir(self._path)

    @property
    def isfile(self):
        return os.path.isfile(self._path)

    @property
    def parrent(self):
        return Leofile(os.path.join(self._path, os.path.pardir))

    @property
    def stat(self):
        return os.stat(self._path)

    def list(self):
        '''
        return listdir
        '''
        return [Leofile(os.path.join(self._path, i)) for i in os.listdir(self._path)]

    def open(self, mode):
        '''
        return opened file
        '''
        return open(self._path, mode)
