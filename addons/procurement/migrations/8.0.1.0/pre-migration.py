# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alexandre Fayolle
#    Copyright 2014 Camptocamp SA
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

from openerp.openupgrade import openupgrade

column_renames = {
        }

xmlid_renames = [
    ('procurement.access_stock_warehouse_orderpoint',
     'stock.access_stock_warehouse_orderpoint')
    ('procurement.access_stock_warehouse_orderpoint_system',
     'stock.access_stock_warehouse_orderpoint_system')
    ('procurement.stock_warehouse_orderpoint_rule',
     'stock.stock_warehouse_orderpoint_rule')
    ('procurement.access_mrp_property',
     'mrp.access_mrp_property'),
    ('procurement.access_mrp_property_group',
     'mrp.access_mrp_property_group')
    ]

@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
    openupgrade.rename_xmlids(cr, xmlid_renames)