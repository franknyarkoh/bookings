from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Room Management"),
			"items": [
				{
					"type": "doctype",
					"name": "House Keeping",
					"label": _("House Keeping"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Room Order"
					"label": _("Room Order"),
					"onboard": 1,
				},
				
			]
		},
		{
			"label": _("Setup"),
			"items": [

				{
					"type": "doctype",
					"name": "Extras",
					"label": _("Extras"),
					"onboard": 1,
					
				},
				{
					"type": "doctype",
					"name": "Floor",
					"label": _("Floor"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Rates",
					"label": _("Rates"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Rooms",
					"label": _("Rooms"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Seasons",
					"label": _("Seasons"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Block",
					"label": _("Block"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Brand Name",
					"label": _("Brand Name"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Locations",
					"label": _("Room Order"),
				},
				{
					"type": "doctype",
					"name": "Property Type",
					"label": _("Room Order"),
				},
				{
					"type": "doctype",
					"name": "Room Type",
					"label": _("Room Order"),
				},
				{
					"type": "doctype",
					"name": "Teams",
					"label": _("Teams"),
					"onboard": 1,
				},
				{
				"type": "doctype",
					"name": "Vehicle Type",
					"label": _("Vehicle Type"),
					"onboard": 1,	
				}
			]
		}
	]
