# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Room Management",
			"category": "Modules",
			"color": "pink",
			"icon": "octicon octicon-home",
			"type": "module",
			"label": _("Room Management"),
			"onboard_present": 1
		}
	]
