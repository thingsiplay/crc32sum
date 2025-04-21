#!/usr/bin/env python3

import argparse
import pathlib
import zlib
import sys


APP_NAME = "crc32sum"
APP_VERSION = "0.1"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Print CRC-32 (binary mode) checksums.",
        epilog="Copyright 2025 Tuncay D. <https://github.com/thingsiplay/crc32sum>",
    )

    _ = parser.add_argument(
        "path",
        default=[],
        nargs="*",
        help=(
            "file or directory, if this is a directory then all top level files"
            " in it are processed, if this is just a '-' character then read"
            " data from stdin instead"
        ),
    )

    _ = parser.add_argument(
        "-r",
        "--resolve",
        default=False,
        action="store_true",
        help="expand relative path to absolute when printing filenames",
    )

    _ = parser.add_argument(
        "-i",
        "--integer",
        default=False,
        action="store_true",
        help="output the checksum in unsigned 32-bit integer format",
    )

    _ = parser.add_argument(
        "-u",
        "--uppercase",
        default=False,
        action="store_true",
        help="output the checksum in uppercase letters",
    )

    _ = parser.add_argument(
        "--version",
        default=False,
        action="store_true",
        help="print version and exit",
    )

    return parser.parse_args()


def crc32sum(data, integer, uppercase):
    sum = zlib.crc32(data)
    if integer:
        return sum
    sum = hex(sum).removeprefix("0x").zfill(8)
    if uppercase:
        sum = sum.upper()
    return sum


def print_file_checksum(path, integer, uppercase):
    try:
        with open(path, "rb") as file:
            print(crc32sum(file.read(), integer, uppercase), " " + path.as_posix())
    except FileNotFoundError:
        eprint(f"{path}: No such file or directory")


def eprint(msg):
    print(f"{APP_NAME}: {msg}", file=sys.stderr)


if __name__ == "__main__":
    args = parse_arguments()

    if args.version:
        print(f"{APP_NAME} v{APP_VERSION}")

    for path in args.path:
        if path == "-":
            data = sys.stdin.buffer.read()
            print(crc32sum(data, args.integer, args.uppercase))
            continue

        try:
            fullpath = pathlib.PosixPath(path).expanduser()
            if args.resolve:
                fullpath = fullpath.resolve()

            if fullpath.is_dir():
                for childpath in fullpath.iterdir():
                    if childpath.is_file():
                        print_file_checksum(childpath, args.integer, args.uppercase)
            else:
                print_file_checksum(fullpath, args.integer, args.uppercase)
        except PermissionError:
            eprint(f"{path}: Permission denied")
