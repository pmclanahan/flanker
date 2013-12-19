""" In memory cache driver. """

from expiringdict import ExpiringDict


class DictCache(ExpiringDict):
    def __getitem__(self, key, with_age=False):
        try:
            return super(DictCache, self).__getitem__(key, with_age)
        except KeyError:
            return None
