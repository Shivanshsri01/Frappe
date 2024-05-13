from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def get_data():
    # Get the count of customers
    data = frappe.get_all("side")
    count = len(data)
    # frappe.msgprint(str(count))
    # Create a JSON object with the count and route options
    return {
        "value": count,
        "fieldtype": "Int",
        "route_options": {"from_date": "2023-05-23"},
        # "route": ["query-report", "Permitted Documents For User"]
    }
