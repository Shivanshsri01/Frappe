// Copyright (c) 2024, Shivansh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("side", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('side', {
    customer: function(frm) {
        if (frm.doc.customer) {
            frappe.call({
                method: 'my_custom_app.my_custom_app.doctype.side.side.get_customer_details',
                args: {
                    customer: frm.doc.customer
                },
                callback: function(response) {
                    var data = response.message;
                    if (data) {
                       
                        frm.set_value('account_manager', data.account_manager);
                        frm.set_value('customer_group', data.customer_group);
                        frm.set_value('currency', data.currency);
                        frm.set_value('price_list', data.price_list);
                    }
                }
            });
        }
    }
});