from flask import Flask, render_template, json, url_for, request
from random import randint
fun = Flask(__name__)

with open('jokeCollection.json') as fp:
    data = json.load(fp)
    
print(type(data))

#print(data['JokeCollection'][0]['catJokes'])
#ids=[]
#for c_id in data:
    #ids.append((c_id['id'], c_id['name']))
#print(ids)
#for item in data['JokeCollection']:
    #print(item['name'])
print(data['JokeCollection'][0]['catJokes'])
