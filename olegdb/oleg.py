import requests, msgpack, hashlib, pickle

DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8080

class OlegDB(object):
    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.host = host
        self.port = port

    def _build_host_str(self, key):
        connect_str = "http://{host}:{port}/{key}".format(
                host=self.host, port=self.port, key=key)
        return connect_str

    def _pack_item(self, value):
        new_value = None
        try:
            new_value = msgpack.packb(value, use_bin_type=True)
        except TypeError as e:
            print e
            new_value = pickle.dumps(value)
        return new_value

    def add(self, key, value, timeout=None):
        resp = requests.get(self._build_host_str(key))
        if resp.status_code == 404:
            self.set(key, value, timeout)
            return True
        return False

    def get(self, key, default=None):
        resp = requests.get(self._build_host_str(key), stream=True)

        if resp.status_code == 404:
            return default

        raw_response = resp.raw.read()
        try:
            return msgpack.unpackb(raw_response, encoding='utf-8')
        except msgpack.ExtraData:
            # Fall back to pickle
            return pickle.loads(raw_response)

    def set(self, key, value, timeout=None):
        new_value = self._pack_item(value)
        connect_str = self._build_host_str(key)

        if timeout is not None:
            expiration = int(time.mktime(time.gmtime())) + timeout
            requests.post(connect_str, data=new_value,
                    headers={"X-OlegDB-use-by": expiration})

        requests.post(connect_str, data=new_value)

    def delete(self, key):
        connect_str = self._build_host_str(key)
        resp = requests.delete(connect_str)

    def get_many(self, keys):
        many = {}
        for key in keys:
            returned = self.get(key, version)
            if returned:
                many[key] = returned
        return many

    def has_key(self, key):
        connect_str = self._build_host_str(key)
        resp = requests.get(connect_str, stream=True)
        if resp.status_code == 404:
            return False
        return True

    def set_many(self, data, timeout=None):
        for key, value in data.iteritems():
            self.set(key, value, timeout)

    def delete_many(self, keys):
        for key in keys:
            self.delete(key, value, timeout)

