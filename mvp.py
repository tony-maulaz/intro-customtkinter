import customtkinter as ctk
from CTkListbox import *

class ContactModel:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def get_contacts(self):
        return self.contacts
    

class ContactView(ctk.CTk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.title("Contact Manager")

        self.label = ctk.CTkLabel(self, text="Name:")
        self.label.pack(pady=5)

        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)

        self.phone_label = ctk.CTkLabel(self, text="Phone:")
        self.phone_label.pack(pady=5)

        self.phone_entry = ctk.CTkEntry(self)
        self.phone_entry.pack(pady=5)

        self.add_button = ctk.CTkButton(self, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=20)

        self.contacts_list = CTkListbox(self)
        self.contacts_list.pack(pady=20)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.presenter.add_contact(name, phone)

    def update_contacts_list(self, contacts):
        self.contacts_list.delete(0, 'end')
        for contact in contacts:
            self.contacts_list.insert('end', f"{contact['name']} - {contact['phone']}")

class ContactPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.presenter = self

    def add_contact(self, name, phone):
        self.model.add_contact(name, phone)
        self.update_contacts_view()

    def update_contacts_view(self):
        contacts = self.model.get_contacts()
        self.view.update_contacts_list(contacts)


if __name__ == "__main__":
    model = ContactModel()
    view = ContactView(None)
    presenter = ContactPresenter(model, view)

    view.mainloop()