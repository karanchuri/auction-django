from django.core.cache import caches


class RedisCacheAdapter:

    @staticmethod
    def set(key, value, timeout=None, machine_alias="default"):
        try:
            _key = key

            if timeout is None:
                _timeout = 60 * 1
            else:
                _timeout = timeout

            cache = caches[machine_alias]
            cache.set(_key, value, timeout=_timeout)
            return True
        except:
            return False

    @staticmethod
    def get(key, machine_alias="default"):
        try:
            cache = caches[machine_alias]
            _value = cache.get(key)
        except:
            _value = None

        return _value

    @staticmethod
    def delete(key, machine_alias="default"):
        try:
            cache = caches[machine_alias]
            cache.delete(key)
        except:
            pass

    @staticmethod
    def get_keys(start_search, machine_alias="default"):
        try:
            cache = caches[machine_alias]
            keys = cache.keys(start_search + '*')
            return keys
        except:
            pass

    @staticmethod
    def delete_collection(start_search, machine_alias="default"):
        try:
            keys = RedisCacheAdapter.get_keys(start_search, machine_alias)
            for key in keys:
                cache = caches[machine_alias]
                cache.delete(key)
            return keys
        except:
            pass
