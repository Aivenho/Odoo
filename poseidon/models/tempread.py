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
    
    ip=fields.Char(string="IP Address",required=True)
    time_intervale=fields.Integer(string="Time Interval")
    data=fields.One2many('temperatures','datas')
    last_update = fields.Datetime('Last update')
    
    def get_temperature(self,cr,uid,context=None):
        temp_obj = self.pool.get('temperatures')

        ids = self.search(cr,uid,[],context=context)
        for rec in self.browse(cr,uid,ids,context=context):
            a = rec.ip
            uu = urllib2.urlopen(a)

            vals_temp = {}
            tree = ET.parse(uu)
            root = tree.getroot()
            for temp in root.findall('SenSet/Entry'):
                id = temp.find('ID').text
                name = temp.find('Name').text
                units = temp.find('Units').text
                value = temp.find('Value').text
                min = temp.find('Min').text
                max = temp.find('Max').text
                newdate = fields.Datetime.now().rpartition(':')[0]
                date_time = datetime.datetime.strptime(newdate,"%Y-%m-%d %H:%M")
                dat_time = date_time.strftime("%Y-%m-%d %H:%M")
                dt_time = str(dat_time).replace('-','.')

                vals_temp = {
                            'id_temp': id,
                            'name': name,
                            'units': units,
                            'value': value,
                            'min': min,
                            'max': max,
                            'datas': rec.id,
                            'datos': fields.Datetime.now(),
                            'dt_time': dt_time,
                }
                flag = temp_obj.create(cr,uid,vals_temp,context=context)
            self.write(cr,uid,ids,{'last_update':vals_temp['datos']})

class temperatures(models.Model):
    _name = 'temperatures'

    id_temp=fields.Integer(string="Sensor ID")
    name=fields.Char(string="Room Name")
    units=fields.Char(string="Units")
    value=fields.Float(string="Actual Value")
    min=fields.Float(string="Min")
    max=fields.Float(string="Max")
    datas=fields.Many2one('Temperature',readonly=True)
    datos=fields.Datetime('Date', required=True,readonly=True)
    dt_time=fields.Char('Date & Time')
