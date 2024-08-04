from flask import Blueprint, render_template, request, redirect, url_for, flash, session
#from models import db, User, Category, Product, Cart, Transaction, Order
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime

# Create a Blueprint for the routes
routes = Blueprint('routes', __name__)

# Define the routes
@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/login')
def login():
    return render_template('login.html')

@routes.route('/register')
def register():
    return render_template('register.html')