from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, \
                  abort, jsonify, make_response
from app.core.repository import *
from app import mysql
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


@mod.route('/textregister')
def textregister():
  return render_template('textregister.html')



@mod.route('/textregister1')
def textregister1():
  return render_template('textregister1.html')

@mod.route('/textregister2')
def textregister2():
  return render_template('textregister2.html')




@mod.route('/lazyimages')
def lazyloading():
  hists = listdir_nohidden('app/static/images/daily')
  hists = ['images/daily/' + file for file in hists]
  return render_template('lazyloading.html',hists = hists)


tasks = [
  {
      'id': 1,
      'title': u'Buy groceries',
      'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
      'done': False
  },
  {
      'id': 2,
      'title': u'Learn Python',
      'description': u'Need to find a good Python tutorial on the web', 
      'done': False
  }
]

@mod.route('/tasks')
def get_tasks():
  return jsonify({'tasks': tasks})

@mod.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
  

@mod.route('/db')
def loco():
  cur = mysql.get_db().cursor()
  cur.execute("SELECT * FROM `AUTHORS`")
  rows = cur.fetchall()

  payload = []
  content = {}
  for row in rows:
      content = {'id': row[0], 'firstName': row[1], 'lastName': row[2]}
      payload.append(content)
      content = {}
  cur.close()
  return jsonify(payload)
    
  



def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f