#!/usr/bin/env python3

"""
/*
 * Copyright (c) 2016 Hailin Su, ISU NBCEC
 *
 * This file is part of sampleBinDumper.
 *
 * sampleBinDumper is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * sampleBinDumper is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU General Lesser Public License
 * along with sampleBinDumper. If not, see <http://www.gnu.org/licenses/>.
 */
"""

import sys
import struct
import os


def usage():
    crtd = "Thu Dec 17 2015 16:43 CDT"  # finished 16:54
    updt = "N/A"
    vers = "0.1"
    bsnm = os.path.basename(sys.argv[0])
    desc = """
    {}

    Prints out content of a binary sample file.

            Author  : hailins@iastate.edu
            Created : {}
            Updated : {}
            Version : {}

    - binary format input file
    - usage:
      {} sampleBIN
      """.format(bsnm, crtd, updt, vers, bsnm)
    print(desc)
    exit(-1)


def main():
    params = sys.argv
    if len(params) != 2:
        usage()

    sample_bin = sys.argv[1]
    n1 = 0
    n2 = 0
    all_samples = b''
    try:
        with open(sample_bin, 'rb') as fp:
            try:
                header = fp.read(4).decode('utf8')
            except UnicodeDecodeError:
                header = 'INVALID HEADER'

            if header != "SAMP":
                print(" [X] HEADER MISMATCHED: {}".format(header))
            else:
                n1 = int.from_bytes(fp.read(4), sys.byteorder)
                n2 = int.from_bytes(fp.read(4), sys.byteorder)  # twice
                fp.seek(fp.tell()+4)
                sample_size = 4*n2
                all_samples = fp.read(sample_size*n1)
    except FileNotFoundError:
        print(" [X] FILE NOT FOUND: {}".format(sample_bin))
    except IsADirectoryError:
        print(" [X] IS A DIRECTORY: {}".format(sample_bin))
    except OSError:
        print(" [X] OS ERROR: {}".format(sample_bin))

    counter = 0
    for element in struct.unpack('f'*n2*n1, all_samples):
        print("{:8.4f}".format(round(element, 4)), end='')
        counter += 1
        if counter % n2 == 0:
            print()
        else:
            print(" ", end='')

main() if __name__ == "__main__" else None
