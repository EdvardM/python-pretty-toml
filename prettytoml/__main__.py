from sys import stdin, stdout

from prettytoml import prettify

stdout.write(prettify(stdin.read()))
