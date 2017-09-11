# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import


characters_file = "../charset/final_common_3500.txt"

with open(characters_file, "r") as f:
    charset = f.readlines()
    charset = [char.strip() for char in charset]
    print(len(charset))