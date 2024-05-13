import frappe
from frappe.model.document import Document
class itemPrice(Document):
    def validate(self):
        frappe.msgprint( "This class is overrided" )