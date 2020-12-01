from flask import Flask, render_template, json, url_for, Response, jsonify, request
from random import random, choice, shuffle
fun = Flask(__name__)

with open('jokeCollection.json') as fp:
    data = json.load(fp)

@fun.route('/', methods = ['GET', 'POST'])
def all():
    if request.method == 'POST':
        prep = data['JokeCollection']
        prep.append(request.json)
        return data
    else:
        return data

@fun.route('/category')
def cat():
    output = "" 
    for item in data['JokeCollection']:
        cat_name = item['name']
        output = output + cat_name +', '
    return output

@fun.route('/category/Allrandom')
def R():
    #pick1fca = {}
    #for item in data['JokeCollection'][id]:
        #joke_content = item['catJokes']
        #pick1fca = pick1fca + joke_content
    All0 = data['JokeCollection'][0]['catJokes']
    All1 = data['JokeCollection'][1]['catJokes']
    All2 = data['JokeCollection'][2]['catJokes']
    Alltogether = All0+All1+All2
    pick1fca = []
    for jj in Alltogether:
        pick1fca.append(jj)
    shuffle(pick1fca)

    return pick1fca.pop()

@fun.route('/category/<int:id>', methods = ['GET', 'POST'])
def cat0(id):
    if request.method == 'POST':
        All0 = data['JokeCollection'][id]['catJokes']
        All0.append(request.json)
        return jsonify(CategoryJokes=All0)
    else:
        All0 = data['JokeCollection'][id]['catJokes']
        return jsonify(CategoryJokes=All0)

@fun.route('/category/<int:id>/catJokes/random')
def cat0R(id):
    All0 = data['JokeCollection'][id]['catJokes']
    pick1f1c = []
    for j in All0:
        pick1f1c.append(j)
    shuffle(pick1f1c)

    return pick1f1c.pop()

@fun.route('/category/0/catJokes/<int:id>')
def cat0_js(id):
    return data['JokeCollection'][0]['catJokes'][id]

@fun.route('/category/1/catJokes/<int:id>')
def cat1_js(id):
    return data['JokeCollection'][1]['catJokes'][id]

@fun.route('/category/2/catJokes/<int:id>')
def cat2_js(id):
    return data['JokeCollection'][2]['catJokes'][id]

if __name__ == "__main__":
    fun.run(debug=True)