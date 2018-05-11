# -*- coding:utf-8 -*-

import sql
from conn import MSSQL
import xlrd
from xlutils.copy import copy
import os


msConn = MSSQL(host="119.23.127.31",user="vpclublnyp_read",pwd="PYT!#661jksw#REWlnyp",port=16188,db='vpclubcloud')
path = u'/Users/fengjianda/Desktop/work/周报/岭南生活报表(2018.05.03).xlsx'


def test():
    need = msConn.ExecQuery(sql.getUser)
    pass


def openExcel():
    data = xlrd.open_workbook(path)
    sheetNameList = []
    for x in range(len(data._sheet_names)-1):
        sheetNameList.append(data._sheet_names[x])
    table1 = data.sheets()[0]
    table2 = data.sheets()[1]

    pass


if __name__ == '__main__':
    oldWb = xlrd.open_workbook(path)
    oldWbS = oldWb.sheet_by_index(2)
    newWb = copy(oldWb)
    newWbs = newWb.get_sheet(2)
    newWbs.write(0,0,'i want to auto')
    newWb.save(u'/Users/fengjianda/Desktop/work/周报/岭南生活报表(2018.05.03)refine.xlsx')


    openExcel()
    test()
