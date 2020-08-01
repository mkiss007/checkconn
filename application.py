import requests
import socket
import os
from flask import Flask,render_template, request, Response


app = Flask(__name__) 
 


@app.route('/', methods=['GET'])
def index():
    return "Hello Chernobyl"
	
@app.route('/mysqldev', methods=['GET'])
def mysql():
   s = socket.socket()
   address = 'hippogriff.mysql.database.azure.com'
   port = 3306  # port number is a number, not string
   try:
      s.connect((address, port)) 
      my_return = ("Connection to %s:%d OK" % (address, port))
      print(my_return)	  
   except Exception as e: 
      my_return = ("something's wrong with %s:%d. Exception is %s" % (address, port, e))
      print(my_return)	  
   finally:
      s.close()
   return(my_return)	

@app.route('/mysqlitst', methods=['GET'])
def mysqlitst():
   s = socket.socket()
   address = 'dokiship.mysql.database.azure.com'
   port = 3306  
   try:
      s.connect((address, port)) 
      my_return = ("Connection to %s:%d OK" % (address, port))
      print(my_return)	  
   except Exception as e: 
      my_return = ("something's wrong with %s:%d. Exception is %s" % (address, port, e))
      print(my_return)	  
   finally:
      s.close()
   return(my_return)	

@app.route('/check/<address>/<int:port>', methods=['GET'])
def check(address,port):
   s = socket.socket()
   try:
      s.connect((address, port)) 
      my_return = ("Connection to %s:%d OK" % (address, port))
      print(my_return)	  
   except Exception as e: 
      my_return = ("something's wrong with %s:%d. Exception is %s" % (address, port, e))
      print(my_return)	  
   finally:
      s.close()
   return(my_return)	

	
@app.route('/wheather',methods=['GET'])
def wheather():
    url = "http://api.openweathermap.org/data/2.5/weather?id=3046526&APPID=8f6abb37f67a3cb3dcef2f6023a92641&units=metric&mode=html"
    response = requests.get(url)
    response.raise_for_status()	
    current_wheather = response.text
    my_html = current_wheather
    return(my_html)	

@app.route('/env', methods=['GET'])
def env():
    my_return = os.environ	
    return(my_return)
