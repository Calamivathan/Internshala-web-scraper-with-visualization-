# export_to_excel.py

import xlwt

style_head = xlwt.easyxf('font: bold 1,height 300;')  
style_body = xlwt.easyxf('font: height 260;')  

def write_header(sheet):
    sheet.write(0, 0, 'Serial No', style_head) 
    sheet.write(0, 1, 'Title', style_head) 
    sheet.write(0, 2, 'Company', style_head) 
    sheet.write(0, 3, 'Location', style_head) 
    sheet.write(0, 4, 'Start By', style_head) 
    sheet.write(0, 5, 'Apply By', style_head) 
    sheet.write(0, 6, 'Duration', style_head) 
    sheet.write(0, 7, 'Stipend', style_head) 
    sheet.write(0, 8, 'Applicants', style_head) 
    sheet.write(0, 9, 'Skills Required', style_head) 
    sheet.write(0, 10, 'Perks', style_head) 
    sheet.write(0, 11, 'Number of Openings', style_head) 
    sheet.write(0, 12, 'Link', style_head)
    sheet.write(0, 13, 'Profile', style_head)  

def write_body(sheet, row_index, data):
    sheet.write(row_index, 0, row_index, style_body)  # Serial No
    sheet.write(row_index, 1, data['internship_title'], style_body)
    sheet.write(row_index, 2, data['company'], style_body)
    sheet.write(row_index, 3, data['location'], style_body)
    sheet.write(row_index, 4, data['start by'], style_body)
    sheet.write(row_index, 5, data['apply by'], style_body)
    sheet.write(row_index, 6, data['duration'], style_body)
    sheet.write(row_index, 7, data['stipend'], style_body)
    sheet.write(row_index, 8, data['applicants'], style_body)
    sheet.write(row_index, 9, data['skills'], style_body)
    sheet.write(row_index, 10, data['perks'], style_body)
    sheet.write(row_index, 11, data['openings'], style_body)
    sheet.write(row_index, 12, data['link'], style_body)
    sheet.write(row_index, 13, data['profile'], style_body)  
