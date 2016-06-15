# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  Interlux, SIA  (http://www.interlux.lv)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Poseidon',
    'version': '8.0.0.0.0',
    'description': 'Temperature Import Module',
    'license': 'AGPL-3',
    'category': 'Tools',
    'author': 'Aivenhoo, Faycal',
        'description': """
Poseidon 2250 (HW group) data import
=================
Solution to integrate temperature
documentation in to Odoo database.
""",
    'depends': [
                ],
    'data': [
            'temperature.xml',
            "security/temperature_user.xml",
            "security/ir.model.access.csv",
             ],
    'application': 'True'
}
