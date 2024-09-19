# 编写报告，修改一个word文档的报告
def write_report():
    # 打开一个现有的Word文档
    doc = Document('模板.docx')

    for para in doc.paragraphs:
        for i in range(len(para.runs)):  # 对于每个段落，遍历其中的每个运行
            # print(para.runs[i].text)  # 打印运行中的文字
            if '特定位置1' in para.runs[i].text:  # 如果运行中的文字包含特定位置2
                para.text = para.text.replace('特定位置1', '111')  # 替换文字
                run = para.add_run()  # 添加文字
                # run.add_picture('1.png', width=Inches(1.0), height=Inches(1.0))  # 添加图片
                run.add_text('添加的文字')  # 添加文字
                run.font.name = '等线'  # 设置字体
                run.font.size = Pt(11)  # 设置字体大小
                run.bold = True  # 设置加粗
                run.font.color.rgb = RGBColor(0, 0, 0)  # 设置字体颜色
                # paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # 设置居中对齐

                # paragraph.clear()  # 清空该段落的内容

                # doc.add_paragraph("下面是一张本地图片：")  # 添加一个段落
                # paragraph.style = 'Title'  # 设置段落样式

                # 添加表格
                '''  
                table = doc.add_table(rows=2, cols=2)            table.cell(0, 0).text = '第一行第一列'  
                table.cell(0, 1).text = '第一行第二列'  
                table.cell(1, 0).text = '第二行第一列'  
                table.cell(1, 1).text = '第二行第二列'  
                '''
                break

                # 在表格中找到对应的文字，之后删除文字，在文字的地方添加上图片
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if '图片1' in cell.text:
                    cell.text = re.sub(r'图片1', '', cell.text)
                    cell.paragraphs[0].add_run().add_picture('1.png', width=Inches(1.0), height=Inches(1.0))
                    cell.paragraphs[0].alignment = 1  # 居中

    tables = doc.tables
    # 获取表格中所有内容对应的坐标
    for i, row in enumerate(tables[0].rows):
        for j, cell in enumerate(row.cells):
            print(f'[+]{cell.text}    [+]对应的坐标是   ({i}, {j})\n')

            # 获取表格中所有内容对应的坐标
    for tab in range(len(tables)):
        tables[tab].cell(0, 0).text = '预习'

        # 保存修改后的文档
    doc.save('modified_example.docx')
