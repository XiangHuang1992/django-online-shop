from raven import Client

from raven import Client

client = Client('http://a5842fe5ef294d3d86d17057c6f2488e:b34fce3c852244759cda90fdf0ccf731@localhost:9000/3')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()