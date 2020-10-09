from sys import stderr, stdin, stdout
from tempfile import TemporaryFile

from prettytoml import prettify


def cli():
    with TemporaryFile("w+", encoding="utf8", prefix="pretty_toml_") as fid:
        pretty_content = prettify(stdin.read())
        fid.write(pretty_content)
        fid.flush()
        fid.seek(0)
        stdout.write(fid.read())
        stdout.flush()
    return 0


if __name__ == "__main__":
    cli()
