from flask import Flask, render_template, json, url_for
fun = Flask(__name__)

with open('jokeCollection3.json') as fp:
    data = json.load(fp)
    #a = print(data['JokeCollection'][0])

@fun.route('/')
def all():
    return data

@fun.route('/category')
def cat():
    for c in data:
        return c

@fun.route('/category/1/catJokes/1')
def cat1_1():
    return data['category']['Collection'][0]

"""
@fun.route('/category/1/catJokes/2')
def cat1_2():
    return data['JokeCollection'][0]['catJokes'][1]

@fun.route('/category/1/catJokes/3')
def cat1_3():
    return data['JokeCollection'][0]['catJokes'][2]

@fun.route('/category/2/catJokes/1')
def cat2_1():
    return data['JokeCollection'][1]['catJokes'][0]
"""

if __name__ == "__main__":
    fun.run(debug=True)