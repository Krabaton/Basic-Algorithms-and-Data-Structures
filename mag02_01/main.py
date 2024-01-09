import argparse
from pathlib import Path
import shutil


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Папка з файлами"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("output"), help="Папка для копіювання"
    )
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    for el in source.iterdir():
        if el.is_dir():
            recursive_copy(el, output)
        else:
            folder = el.name[:1]
            folder = output / folder
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy(el, folder)


def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)
    print(args)


if __name__ == "__main__":
    main()
