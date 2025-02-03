from pysnmp.smi.error import NoAccessError

from dairyProject.entry import Entry


class Dairy:
    def __init__(self, fullname, pin):

        self.entries = []
        self.fullname = fullname
        self.pin = pin
        self.counter = 0
        self.is_locked = False


    def add_entry(self, title, body):
        if self.is_locked: raise NoAccessError
        if title == "": raise ValueError("Title cannot be an empty string")
        if body == "": raise ValueError("Body cannot be an empty string")
        self.counter += 1
        self.entries.append(Entry(self.counter, title, body))

    def my_size(self):
        return len(self.entries)

    def lock(self):
        self.is_locked = True

    def is_lock(self):
        return self.is_locked

    def unlock(self, pin):
        if pin != self.pin: raise TypeError('pin is not pin')
        self.is_locked = False

    def get_fullname(self):
        if self.is_locked: raise ValueError('pin is locked')
        return self.fullname

    def set_fullname(self, param):
        self.fullname = param

    def find_entry_by_id(self, id):
        if id <= 0: raise ValueError('id must be greater than zero')
        for entry in self.entries:
            if entry.get_id() == id: return entry
        raise IndexError

    def delete_entry_by_Id(self, id):
        entry = self.find_entry_by_id(id)
        if entry is not None:
            self.entries.remove(entry)

    def update_entry_by_id(self, id, title, body):
        if self.is_locked: raise ValueError('pin is locked')
        entry = self.find_entry_by_id(id)
        if entry is not None:
            entry.title = title
            entry.body = body
