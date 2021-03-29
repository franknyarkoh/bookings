// Copyright (c) 2019, Frank Nyarkoh and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Room Order', {
//	refresh: function(frm) {
//
//	}
//});

frappe.ui.form.on("Room Order", "refresh", function(frm, cdt, cdn){
var d = locals[cdt][cdn];   
frappe.model.set_value(cdt, cdn, "booking_nights", frappe.datetime.get_day_diff( d.booking_checkout , d.booking_checkin));
    refresh_field("booking_nights");
});
