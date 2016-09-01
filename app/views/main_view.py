from flask import request,jsonify,render_template,send_file

from app import app
from app import colorize


# curl -H "Content-Type: application/json" -X POST "http://127.0.0.1:5000/" -d '{"src":"filurl","color":"102,51,0","method":"overlay"}'
@app.route('/', methods=['POST'])
def index():
    try:
        if request.json['method'] == 'overlay':
            colorize.image_overlay(request.json['src'], request.json['color']).save('app/static/res.png')
        elif request.json['method'] == 'color':
            colorize.image_color(request.json['src'], request.json['color']).save('app/static/res.png')
        elif request.json['method'] == 'multiply':
            colorize.image_multiply(request.json['src'], request.json['color']).save('app/static/res.png')
        else:
            colorize.image_color(request.json['src'], request.json['color']).save('app/static/res.png')
        return jsonify('{{"result":{0}}}'.format("/satatic/res.png"))
    except Exception as e:
        return jsonify('{{"error":{0}}}'.format(e))

@app.route('/res',methods=['GET'])
def result():
    return send_file('app/static/res.png')

