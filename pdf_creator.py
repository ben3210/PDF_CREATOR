from fpdf import FPDF
import os

header_title  = 'Homework Assignments'
logo = 'images/logos.svg'
tasks = os.listdir('tasks')


class PDF(FPDF):
    def header(self):
        #logo
        self.image(logo , 10, 8, 14)
        self.set_font('helvetica', 'B', 14)
        #Title
        self.cell(50) #blank cell - for padding (Moving title to the centre)
        self.set_draw_color(200,0,0)
        self.set_fill_color(57,120,255)
        self.set_text_color(255, 255, 255)
        self.cell(100, 10, header_title , border=0, align='C', fill=1)
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(120, 120, 120)
        self.cell(0,10, 'Prepared by: Benjamin Irabisohoje', align='L')
        self.cell(0, 10, f"Page {self.page_no()} / {{nb}}", align='R')

    def task_content(self, task):
        self.add_page()
        with open(f'tasks/{task}', 'r') as task:
            txt = task.read()
        #Title
        self.set_font('helvetica', 'B', 14)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'{task.name}', ln=1)
        #Code - Task Content
        self.set_text_color(0, 0, 0)
        self.set_font('courier', '', 10)
        self.multi_cell(0, 5, txt, border=1)

pdf = PDF('P', 'mm', 'Letter')
pdf.alias_nb_pages() # for calculating total number of pages

pdf.set_auto_page_break(auto=1, margin=15)
for task in tasks:
    pdf.task_content(task)

pdf.output('Book.pdf')