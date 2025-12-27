## Put and Delete HTTP verbs
## Working with API's

from flask import Flask,jsonify,request

app = Flask(__name__)

# Initial data to my to-do list
items = [
    {'id':1,'name':'Item1','description':"This is Item 1"},
    {'id':2,'name':'Item2','description':"This is Item 2"},
    {'id':3,'name':'Item3','description':"This is Item 3"}
]

@app.route('/')
def home():
    return "Welcome to the sample To-Do List App"

# Retrieve all items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# Retrieve specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item_by_id(item_id):
    item  = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item is not found! "})
    else:
        return jsonify(item)
    
# POST: Create a new task
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'JSON Item not found or Name is not in json'})
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item  = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id']!=item_id]  
    return jsonify({'result':'Item deleted'})  

if __name__=="__main__":
    app.run(debug='True')