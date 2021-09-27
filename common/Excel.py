#!/usr/bin/env python
# encoding: utf-8
import openpyxl
class Excle():
    def __init__(self,file_name):
        self.file_name=file_name
        self.workbook=None
    #打开Excel
    def open_excle(self):
        workbook=openpyxl.load_workbook(self.file_name)
        self.workbook=workbook
        return workbook
    #获取表单
    def get_excle(self,Form):
        workbook=self.open_excle()
        sheet=workbook[Form]
        return sheet
    #读取表单的数据
    def read_excle(self,Form):
        sheet=self.get_excle(Form)
        rows=list(sheet.rows)
        data=[]
        headers=[]
        for title in rows[0]:
            headers.append(title.value)
        for row in rows[1:]:
            d={}
            for x,y in enumerate(row):
                d[headers[x]]=y.value
            data.append(d)
        self.close_excle()
        return data
    #写入Excel的数据：
    def write_excle(self,Form,row,column,data):
        sheet=self.get_excle(Form)
        sheet.cell(row,column).value=data
        self.save_excle()
        self.close_excle()
    #保存Excel
    def save_excle(self):
        self.workbook.save(self.file_name)
    #关闭Excel
    def close_excle(self):
        self.workbook.close()
