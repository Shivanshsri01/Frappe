# Copyright (c) 2024, Shivansh and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _ 
from frappe.model.document import Document


class side(Document):
    def validate(self):
        # Check if the checkbox is checked and both First Name and Last Name are filled
        if self.first_name and self.last_name and self.box :
            # Set the Full Name field to the concatenation of First Name and Last Name
            self.full_name = f"{self.first_name} {self.last_name}"
        else:
            # If validation fails, raise an error
            frappe.throw("Please select field")
            
            
@frappe.whitelist()
def get_customer_details(customer):
    customer_doc = frappe.get_doc('Customer', customer)
    data = {
        'account_manager': customer_doc.account_manager,
        'customer_group': customer_doc.customer_group,
        'currency': customer_doc.default_currency,
        'price_list': customer_doc.default_price_list
    }
    return data


@frappe.whitelist(allow_guest=True)
def get_name_details(customer):
    customer_doc = frappe.get_doc('Customer', customer)
    data = {
       'customer_name': customer_doc.customer_name,
       'customer_group': customer_doc.customer_group
    }
    return data


@frappe.whitelist(allow_guest=True)
def create(first_name, last_name, box):
    try:
        # Convert value to an integer (0 or 1)
        box = int(box)

        # Validate value
        if box not in (0, 1):
            return {"error": "value must be 0 or 1"}

        # Create a new Custom Doc based on the received data
        side = frappe.new_doc('side')
        side.first_name = first_name
        side.last_name = last_name
        side.box = box
        side.insert()

        return {"message": "created successfully"}
    except Exception as e:
        return {"error": str(e)}

@frappe.whitelist(allow_guest=True)
def update(docname, first_name):
    try:
        # Load the existing Custom Doc
        doc = frappe.get_doc('side', docname)

        # Update the fields with the new values
        doc.first_name = first_name
        
        doc.save()

        return {"message": " updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    
    
@frappe.whitelist(allow_guest=True)
def delete(docname):
    try:
        # Load the existing Custom Doc
        doc = frappe.get_doc('side', docname)

        # Delete the document
        doc.delete()

        return {"message": " deleted successfully"}
    except Exception as e:
        return {"error": str(e)}
    

from frappe.model.meta import get_meta
@frappe.whitelist(allow_guest=True)
def get_user_info_with_doctypes():
    try:
        # Get user doctypes
        user_doctypes = [d.name for d in frappe.get_all("DocType", filters={"module": "User"})]

        # Get user information
        user_info = frappe.get_all("User", fields=["full_name", "enabled", "name"])

        return {"user_doctypes": user_doctypes, "user_info": user_info}
    except Exception as e:
        return {"error": str(e)}

@frappe.whitelist(allow_guest=True)
def create_user(email, full_name):
    try:
        # Create a new User
        user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": full_name,
            #"custom_field": custom_field_value
        })
        user.insert(ignore_permissions=True)

        return {"message": _("User created successfully")}
    except Exception as e:
        return {"error": str(e)}
