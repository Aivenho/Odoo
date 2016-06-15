# -*- coding: utf-8 -*-

from openerp import fields, models, api, _
from tempfile import TemporaryFile
import base64
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT
from lxml import etree
import xml.etree.ElementTree as ET
import urllib2
import os,time
import datetime,parser

class temperature(models.Model):
    _name= 'temperature'
    
    ip=fields.Char(string="Ip",required=True)
    time_intervale=fields.Integer(string="Time intervale")
    data=fields.One2many('temperatures','datas')
    
    def get_temperature(self, cr, uid, context=None):
        temp_obj = self.pool.get('temperatures')
        print  "contextcontext",context

        ids = self.search(cr, uid,[], context=context)
        for rec in self.browse(cr, uid, ids, context=context):
            print '\n\n\n*****',rec, rec.id  
            a=rec.ip
            print a
            uu=urllib2.urlopen(a)

            vals_temp = {}
            tree = ET.parse(uu)
            root = tree.getroot()
            for temp in root.findall('SenSet/Entry'):
                id=temp.find('ID').text
                name=temp.find('Name').text
                units=temp.find('Units').text
                value=temp.find('Value').text
                min=temp.find('Min').text
                max=temp.find('Max').text
                print id,name,units,value,min,max
                vals_temp = {
                            'id_temp': id,
                            'name': name,
                            'units':units,
                            'value':value,
                            'min':min,
                            'max':max,
                            'datas':rec.id,
                            'datos':fields.Datetime.now(),}
                temp_obj.create(cr,uid,vals_temp,context=context)                
           

class temperatures(models.Model):
    _name= 'temperatures'
    def set_datato_dt_time(self):
		res = {}
		res = {}.fromkeys(self.ids, '')
		for obj in self:
			date_time = datetime.datetime.strptime(obj.datos, "%Y-%m-%d %H:%M:%S")
			dt_time = date_time + datetime.timedelta(minutes = 0, hours = 0)
			obj.write({'dt_time':str(dt_time).replace('-','/')})
			res[obj.id] = 1.0
		return res
    id_temp=fields.Integer(string="Sensor ID")
    name=fields.Char(string="Room Name")
    units=fields.Char(string="Units")
    value=fields.Float(string="Actual Value")
    min=fields.Float(string="Min")
    max=fields.Float(string="Max")
    datas=fields.Many2one('temperature',readonly=True)  
    datos = fields.Datetime('Date', required=True,readonly=True)
    fill_data = fields.Float(compute=set_datato_dt_time,string="Child Service")
    dt_time = fields.Char('Date & Time')
