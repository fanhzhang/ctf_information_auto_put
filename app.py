#coding:utf-8 
from flask import Flask, request, render_template , url_for
import os
app = Flask(__name__)
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def  writeupsth(filename,text):
  file = open(filename, 'a')
  file.write(text)
  file.close()

def readupsth(filename):
  file = open(filename,'r')
  return file.readlines()

@app.route('/blog_get', methods=['GET', 'POST'])
def home():
  title_url_dic = {}
  try:
    # title_url_str = readupsth('url.txt')[0]
    # title_url_dic = eval(title_url_str)
    for line in readupsth('url.txt'):
      title_url_dic = dict(title_url_dic.items()+eval(line).items())
  except:
    pass
  return render_template('home.html',title_url_dic=title_url_dic)


@app.route('/ctf_game', methods=['GET', 'POST'])
def ctf():
  ctf_games = readupsth('ctf_game.txt')
  data = zip(eval(ctf_games[0]),eval(ctf_games[1]),eval(ctf_games[2]))
  return render_template('ctf.html',data=data)


@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('test.html')
if __name__ == '__main__':
  app.run(debug=True) 