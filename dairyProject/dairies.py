from boto.kms.exceptions import AlreadyExistsException

from dairyProject.dairy import Dairy

class Dairies:
    def __init__(self):
        self.dairies = []

    def add_dairy(self, fullname, pin):
        if fullname == "": raise ValueError("Full name cannot be empty")
        if pin == "": raise ValueError("Pin cannot be empty")
        if self.find_dairy_by_username(fullname): raise AlreadyExistsException("Dairy with fullname '{}' already exists".format(fullname))
        dairy = Dairy(fullname, pin)
        self.dairies.append(dairy)

    def find_dairy_by_username(self, username):
        if len(self.dairies) == 0: raise ValueError("No dairies found")
        for dairy in self.dairies:
            if dairy.username == username:
                return dairy

    def delete_dairy_by_username(self, username):
        if len(self.dairies) == 0: raise ValueError("No dairies found")
        for dairy in self.dairies:
            if dairy.username == username:
                self.dairies.remove(dairy)
