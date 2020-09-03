#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  sys

import os
import sys

win32 = sys.platform.startswith('win')

if win32:
    # print(sys.executable)
    sub_path, file_name = os.path.split(sys.executable)
print(sub_path)
print(file_name)
