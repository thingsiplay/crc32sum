# crc32sum

Print CRC-32 (binary mode) checksums.

- Author: Tuncay D.
- Source: [Github](https://github.com/thingsiplay/crc32sum)
- License: [MIT License](LICENSE)

## What is this program for?

Calculates the
[CRC hash](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) for each 
given file, using
[Python's integrated zlib module](https://docs.python.org/3/library/zlib.html#zlib.crc32).
It has a similar use like MD5 or SHA, but is way, way weaker and simpler. It's
a quick and easy method to verify the integrity of files, in example after 
downloading from the web, to check data corruption from your external drives 
or when creating expected files.

It is important to know and understand that CRC-32 is not secure and should
never be used cryptographically. It's use is limited for very simple use cases.

Linux does not have a standard program to calculate the CRC. This is a very
simple program to have a similar output like `md5sum` offers by default.

## Why use CRC at all?

Usually and most of the time CRC is not required to be used. In fact, I favor
MD5 or SHA when possible. But sometimes, only a CRC is provided (often used by
the retro emulation gaming scene). Theoretically CRC should also be faster than
the other methods, but no performance comparison has been made (frankly the
difference doesn't matter to me).

## Requirements

This script was originally written with Python 3.13 for Linux, but will be
probably work with older versions of Python as well. No other Python module
or applications are required.

## Installation

No special installation setup or routine required. Give `crc32sum.py` the
executable bit, rename the script to exclude it's file extension and put it
into a directory found in the systems $PATH (in example find out locations
in use for your executables with command `env | grep ^PATH=`).

```
git clone https://github.com/thingsiplay/crc32sum
cd crc32sum
chmod +x crc32sum.py
mv crc32sum.py crc32sum
./crc32sum --help
```

## Usage

```
usage: crc32sum [-h] [-r] [-i] [-u] [--version] [path ...]
```

This is a commandline application without a graphical interface. The most basic
operation is to give it a filename, a list of files or directories to work on.
The program will calculate the CRC for each file and output the checksum and
filename or path in a similar format like `md5sum` does by default.

If the input is a directory, then all files (without being recursive) in it
are processed. If there is a single dash `-`, then it means use the data from
stdin to calculate checksum (empty filename in the listing).

### Examples 

```
crc32sum *.sfc
2d206bf7  Chrono Trigger (USA).sfc

crc32sum --resolve --upper *.sfc
2D206BF7  /home/tuncay/Projects/crc32sum/Chrono Trigger (USA).sfc

echo "hello world" | crc32sum -
af083b2d
```

