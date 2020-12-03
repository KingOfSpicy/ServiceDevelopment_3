from flask import Flask, render_template, json, url_for, Response, jsonify, request
from random import random, choice, shuffle
fun = Flask(__name__)

with open('jokeCollection.json') as fp:
    data = json.load(fp)

@fun.route('/', methods = ['GET', 'POST'])
def all():
    #lst = ['item']*10
    if request.method == 'POST':
        prep = data['JokeCollection']
        prep.append(request.json)
        return data
        #return render_template('home.html', len=len(lst), data=data)
        #return render_template('home.html', data=data)
    else:
        return data
        #return render_template('home.html', len=len(lst), data=data)
        #return render_template('home.html', data=data)

@fun.route('/category')
def cat():
    output=[]
    for x in data['JokeCollection']:
        #for y in x['name']:
        output.append(x['name'])
        json_categories = json.dumps(output)
    return json_categories
    #return render_template('cats.html', len=len(output), output=output)
    #output = "" 
    #for item in data['JokeCollection']:
        #cat_name = item['name']
        #output = output + cat_name +'<br/>'+'<br/>'
    #return output

@fun.route('/category/Allrandom')
def R():
    pick1fca = []
    for x in data['JokeCollection']:
        for y in x['catJokes']:
            pick1fca.append(y)
    shuffle(pick1fca)
    getContent = pick1fca.pop()
    return getContent
    #return render_template('randomj.html', like=getContent['like'],  dislike=getContent['dislike'], onejoke=getContent['content'])

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

    #return render_template('onejoke.html', onejoke=pick1f1c)
    return pick1f1c.pop()

@fun.route('/category/<int:id>/catJokes')
def cat_takeAlljokes(id):
    output=[]
    for x in data['JokeCollection'][id]['catJokes']:
        jj = x['content']
        output.append(jj)
    json_thisCjokes = json.dumps(output)
    return json_thisCjokes
    #return render_template('categoryjoke.html', len=len(output), output=output)

@fun.route('/category/0/catJokes/<int:id>', methods = ['GET', 'POST'])
def cat0_js(id):
    if request.method == 'POST':
        if request.form.get('submit_a'):
            data['JokeCollection'][0]['catJokes'][id]['like'] = data['JokeCollection'][0]['catJokes'][id]['like']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][0]['catJokes'][id]['content']
            like = data['JokeCollection'][0]['catJokes'][id]['like']
            dislike = data['JokeCollection'][0]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            return data['JokeCollection'][0]['catJokes'][id]

        elif request.form.get('submit_b'):
            data['JokeCollection'][0]['catJokes'][id]['dislike'] = data['JokeCollection'][0]['catJokes'][id]['dislike']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][0]['catJokes'][id]['content']
            like = data['JokeCollection'][0]['catJokes'][id]['like']
            dislike = data['JokeCollection'][0]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            #return render_template('onejoke.html', onejoke=onejoke)
            return data['JokeCollection'][0]['catJokes'][id]
            
    else:
        #like = data['JokeCollection'][0]['catJokes'][id]['like']
        #dislike = data['JokeCollection'][0]['catJokes'][id]['dislike']
        #onejoke = data['JokeCollection'][0]['catJokes'][id]['content']
        #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
        return data['JokeCollection'][0]['catJokes'][id]



@fun.route('/category/1/catJokes/<int:id>', methods = ['GET', 'POST'])
def cat1_js(id):
    if request.method == 'POST':
        if request.form.get('submit_a'):
            data['JokeCollection'][1]['catJokes'][id]['like'] = data['JokeCollection'][1]['catJokes'][id]['like']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][1]['catJokes'][id]['content']
            like = data['JokeCollection'][1]['catJokes'][id]['like']
            dislike = data['JokeCollection'][1]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            #return render_template('onejoke.html', onejoke=onejoke)
            return data['JokeCollection'][1]['catJokes'][id]



        elif request.form.get('submit_b'):
            data['JokeCollection'][1]['catJokes'][id]['dislike'] = data['JokeCollection'][1]['catJokes'][id]['dislike']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][1]['catJokes'][id]['content']
            like = data['JokeCollection'][1]['catJokes'][id]['like']
            dislike = data['JokeCollection'][1]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            #return render_template('onejoke.html', onejoke=onejoke)
            return data['JokeCollection'][1]['catJokes'][id]

            
    else:
        #like = data['JokeCollection'][1]['catJokes'][id]['like']
        #dislike = data['JokeCollection'][1]['catJokes'][id]['dislike']
        #onejoke = data['JokeCollection'][1]['catJokes'][id]['content']
        #return render_template('onejoke.html', onejoke=onejoke)
        return data['JokeCollection'][1]['catJokes'][id]


@fun.route('/category/2/catJokes/<int:id>', methods = ['GET', 'POST'])
def cat2_js(id):
    if request.method == 'POST':
        if request.form.get('submit_a'):
            data['JokeCollection'][2]['catJokes'][id]['like'] = data['JokeCollection'][2]['catJokes'][id]['like']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][2]['catJokes'][id]['content']
            like = data['JokeCollection'][2]['catJokes'][id]['like']
            dislike = data['JokeCollection'][2]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            return data['JokeCollection'][2]['catJokes'][id]



        elif request.form.get('submit_b'):
            data['JokeCollection'][2]['catJokes'][id]['dislike'] = data['JokeCollection'][2]['catJokes'][id]['dislike']+1
            with open('jokeCollection.json', 'w') as fp:
                json.dump(data, fp)
            onejoke = data['JokeCollection'][2]['catJokes'][id]['content']
            like = data['JokeCollection'][2]['catJokes'][id]['like']
            dislike = data['JokeCollection'][2]['catJokes'][id]['dislike']
            #return render_template('onejoke.html', like=like, dislike=dislike, onejoke=onejoke)
            #return render_template('onejoke.html', onejoke=onejoke)
            return data['JokeCollection'][2]['catJokes'][id]

            
    else:
        #like = data['JokeCollection'][2]['catJokes'][id]['like']
        #dislike = data['JokeCollection'][2]['catJokes'][id]['dislike']
        #onejoke = data['JokeCollection'][2]['catJokes'][id]['content']
        #return render_template('onejoke.html', onejoke=onejoke)
        return data['JokeCollection'][2]['catJokes'][id]


if __name__ == "__main__":
    fun.run(debug=True)