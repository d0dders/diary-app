
from collections import OrderedDict
import datetime
from peewee import *

db = SqliteDatabase('diary.db')




class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    #ceat db and table if don't exist
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry."""


def view_entries():
    """View entries."""


def delete_entry(entry):
    """Delete an entry"""


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries)    
])


if __name__ == "__main__":
    initialize()
    menu_loop()