from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route('/HelloWorld')
def hello_world():
    return 'Hello World'

contacts=[
    {
        'id':1,
        'name':'Arko',
        'number':'6291'
        
    },
    {
        'id':2,
        'name':'Arko2',
        'number':'9632'

    }
]
@app.route('/get-contact')
def get_contact():
    return jsonify({
        'data':contacts
    })



@app.route('/add-contact',methods=['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },400)
    contact={
        'id':contacts[-1]['id']+1,
        'name':request.json['name'],
        'number':request.json.get('number','')
        
    }
    contacts.append(contact)
    return jsonify({
            'status':'success',
            'message':'contact added succesfully'
        }) 

if(__name__=='__main__'):
    app.run(debug=True)