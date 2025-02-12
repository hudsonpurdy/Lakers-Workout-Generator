from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource
import os

app = Flask(__name__)

data = DataSource()

@app.route('/')
def returnHomepage():
    '''Renders homepage with instructions'''
    return render_template("index.html")


@app.route('/search', methods=['GET','POST'])
def returnSearch():
    '''Renders search page. If there is a post request, it processes the data and updates the page.'''
    if request.method == 'POST':
        equipment = request.form['equipmenttype']
        muscle = request.form['musclegroup']
        return render_template("search.html")
    return render_template("search.html")


@app.route('/results', methods=['GET', 'POST'])
def returnResults():
    '''Renders results page. Iterates through results using datasource.py and posts information on results page.'''
    equipment=request.form['equipmenttype']
    muscle=request.form['musclegroup']
    results = set(data.getExerciseByMuscle(muscle))&set(data.getExerciseByEquipment(equipment))
    outlist=[]
    for result in results:
        outlist.append(result[0])
    return render_template('results.html', results=urlPairs(outlist), equipment=equipment, muscle=muscle)


def urlPairs(outlist):
    '''Returns a dictionary with keys equal to exercise names and values equal to corresponding 
    description URLs. Allows for clickable URLs on results page.'''
    pairs = {}
    for name in outlist:
        if name not in pairs.keys():
            pairs[name] = data.getURLByName(name)[0][0]
    
    return pairs

@app.route('/diagram', methods=['GET', 'POST'])
def returnDiagram():
    '''Renders a diagram of the muscles on a body.'''
    return render_template('diagram.html')


@app.errorhandler(404)
def page_not_found(e):
   '''Returns a page not found error message.'''
   return render_template('404.html')


@app.errorhandler(500)
def python_bug(e):
   '''Returns a python bug error message'''
   return render_template('pythonbug.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5123)
    
