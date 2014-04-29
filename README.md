Installation
============

```bash
python setup.py install
````

Usage
=====

```Python
from olegdb import OlegDB, DEFAULT_HOST, DEFAULT_PORT

# default_host and default port are optional
connection = OlegDB()

connection.set("test", 123)
connection.get("test")
````

Thats the gist. There are a couple other methods, the code is pretty clear.
