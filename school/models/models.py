# -*- coding: utf-8 -*-


from odoo import models, fields, api


class student(models.Model):
     _name = 'school.student'
     _description = 'school.school'

     name = fields.Char(string="nom", required=True, help="Prova del help")
     value = fields.Integer()
     description = fields.Text("Moixolo ja està aci")
     last_login = fields.Datetime()

     foto = fields.Binary()
     foto_2 = fields.Image(max_with=200, max_heigth=200)
     clasroom = fields.Many2one('school.clasroom')

class clasroom(models.Model):
     _name = 'school.clasroom'
     _description = 'classes on van el alumnes'
     name = fields.Char()

     student = fields.One2many('school.student', 'clasroom')

#class Teacher(models.Model):
#     _name = 'school.teacher'
#     _description = 'Un professor qualsevol' 
#
#     name = fields.Char()
#     clasroom = fields.Many2many('school.clasroom')