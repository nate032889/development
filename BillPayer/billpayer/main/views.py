from billpayer.main.forms import ItemTable
from flask import render_template, url_for, flash, redirect, request, Blueprint


main = Blueprint('main', __name__)


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


@main.route("/", methods=['GET', 'POST'])
@main.route("/payer", methods=['GET', 'POST'])
def payer():

    items = [Item('Name1', 'Description1'),
             Item('Name2', 'Description2'),
             Item('Name3', 'Description3')]

    table = ItemTable(items)

    return render_template('main.html', tables=table)
