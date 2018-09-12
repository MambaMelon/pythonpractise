# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 13:56
# @Author  : melon

import xlrd

if __name__ == '__main__':

    files = './datasets/excel.xls'
    wb = xlrd.open_workbook(files)
    ws = wb.sheet_by_name('Sheet1')
    cell = ws.cell(1, 2)
    print(cell.ctype)
    print(cell.value)
    dataset = []
    for r in range(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        dataset.append(col)

    print(dataset)


