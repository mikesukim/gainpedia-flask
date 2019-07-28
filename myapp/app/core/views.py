from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify
from app.core.repository import *
import os, sys

mod = Blueprint('core', __name__)


@mod.route('/')
def index():
  return "HELLO MICHAEL!!"
  
@mod.route('/tutorial')
def tutorial():
  repository = Repository()
  return (render_template('core/index.html', resources=repository.getResources()))

@mod.route('/register')
def register():
  return (render_template('Register/register.html'))


@mod.route('/images')
def images():
  hists = listdir_nohidden('app/static/images/daily')
  hists = ['images/daily/' + file for file in hists]
  return render_template('images.html', hists = hists)

@mod.route('/jiyun')
def jiyun():
  return (render_template('jiyun.html'))

@mod.route('/jiyun1')
def jiyun1():
  hists = listdir_nohidden('app/static/images/daily')
  hists = ['images/daily/' + file for file in hists]
  return render_template('jiyun.html', hists = hists)








def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f