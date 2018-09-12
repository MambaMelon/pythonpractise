# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 13:56
# @Author  : melon

import xlrd

if __name__ == '__main__':

    file = './datasets/excel.xls'
    wb = xlrd.open_workbook(file)
    ws = wb.sheet_by_name('Sheet1')

    dataset = []
    for r in range(ws.nrows):
        col = []
        for c in range(ws.ncols):
            col.append(ws.cell(r, c).value)
        dataset.append(col)

    print(dataset)


