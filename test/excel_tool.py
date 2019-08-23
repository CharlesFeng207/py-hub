from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
import requests
from requests import Response
import os
import sys

path_src = sys.argv[1]
print(path_src)

workbook_src = load_workbook(path_src)
shert_name = list(filter(lambda x:x[0] != '@' and x[0] != '#', workbook_src.sheetnames))[0]
print(shert_name)

sheet_src = workbook_src[shert_name]

target_cols = []
i = 1
while True:
    cell = sheet_src["{}{}".format(get_column_letter(i), 2)]
    if cell.value is None:
        break
    if cell.comment is not None and "@language" in cell.comment.content:
        target_cols.append(get_column_letter(i))
    i+=1

print(target_cols)

for target_letter in target_cols:
    type_cell = sheet_src["{}{}".format(target_letter, 2)]
    type_cell.comment = Comment("done!", "excel_tool")
    type_cell.value = "int32"

    for row in range(5, sheet_src.max_row + 1):
        cell = sheet_src["{}{}".format(target_letter, row)]
        print(cell.value)
        if cell.value is not None:
            respond = None
            while True:
                 respond = requests.get('http://139.155.88.114:5000/query', {"content":cell.value})
                 if respond.status_code == 200:
                     break
            print(respond.text)
            cell.comment = Comment(cell.value, "excel_tool")
            cell.value = respond.text
        else:
            cell.value = 0


# sheet_type = workbook_src["@Types"]
# sheet_type["A1"].value = sheet_type["A1"].value
workbook_src.save(os.path.basename(path_src))

input("complete!")
