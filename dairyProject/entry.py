from datetime import datetime

class Entry:

    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.date = datetime


    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_body(self, body):
        self.body = body

    def set_title(self, title):
        self.title = title

    def __str__(self):
        return f"entry id: {self.id}\n title: {self.title} \n body: {self.body} \n date: {self.date}"