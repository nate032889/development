from flask import render_template, url_for, flash, redirect, request, Blueprint


auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    return f"""
    Login Page
    """
