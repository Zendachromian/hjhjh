from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from app import app

from functools import wraps
from datetime import datetime


# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')