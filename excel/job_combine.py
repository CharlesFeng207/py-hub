# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
import time
import json
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
import os
from openpyxl.styles import PatternFill, colors


if __name__ == "__main__":
    outputFolder = "done"
    files = os.listdir(outputFolder)
    pending = {} # id -> {} (cn en bgcolor)
    for i,filename in enumerate(files):
        print("process {}, {} / {}".format(filename, i+1, len(files)))
        workbook_p = load_workbook(os.path.join(outputFolder, filename)), data_only=True)
        s = workbook_p["work"]
        for row in range(1, s.max_row + 1):
            obj = {"cn":s["A{}".format(row)], "en":s["B{}".format(row)], }

    path_src = "Language.xlsx"
    workbook_src = load_workbook(path_src, data_only=True)
    shert_name = list(filter(lambda x:x[0] != '@' and x[0] != '#', workbook_src.sheetnames))[0]

    sheet_src = workbook_src[shert_name]

    target_letter = "B"
    start_row = 3
    
    total = 0
    for row in range(start_row, sheet_src.max_row + 1):
        cell = sheet_src["{}{}".format(target_letter, row)]
        if cell.value is None:
            continue

    
        
    print("done!")