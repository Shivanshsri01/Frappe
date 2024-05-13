# Copyright (c) 2024, Shivansh and contributors
# For license information, please see license.txt






from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def execute(filters=None):
    columns = [
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer"},
        {"label": "Sales Order", "fieldname": "name", "fieldtype": "Link", "options": "Sales Order"},
        {"label": "Delivery Date", "fieldname": "delivery_date", "fieldtype": "Date"},
        {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data"},
        {"label": "Item Quantity", "fieldname": "qty", "fieldtype": "Float"}
    ]

    data = frappe.get_all("Sales Order", filters=filters, fields=["name", "customer", "delivery_date"])
    result = []
    for order in data:
        items = frappe.get_all("Sales Order Item", filters={"parent": order.name}, fields=["item_code", "item_name", "qty"])
        for item in items:
            result.append({
                "customer_name": order.customer,
                "name": order.name,
                "delivery_date": order.delivery_date,
                "item_code": item.item_code,
                "item_name": item.item_name,
                "qty": item.qty
            })

    return columns, result