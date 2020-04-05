from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "House Keeping",
				},
				{
					"type": "doctype",
					"name": "Room Order"
				},
				
			]
		},
		{
			"label": _("Setup"),
			"items": [

				{
					"type": "doctype",
					"name": "Extras"
				},
				{
					"type": "doctype",
					"name": "Floor"
				},
				{
					"type": "doctype",
					"name": "Rates"
				},
				{
					"type": "doctype",
					"name": "Rooms"
				},
				{
					"type": "doctype",
					"name": "Seasons"
				},
				{
					"type": "doctype",
					"name": "Block"
				},
				{
					"type": "doctype",
					"name": "Brand Name"
				},
				{
					"type": "doctype",
					"name": "Locations"
				},
				{
					"type": "doctype",
					"name": "Property Type"
				},
				{
					"type": "doctype",
					"name": "Room Type"
				},
				{
					"type": "doctype",
					"name": "Teams"
				}
			]
		}
	]
