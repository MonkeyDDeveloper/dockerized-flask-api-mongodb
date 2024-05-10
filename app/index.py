from flask import Flask, Response, request
from bson.objectid import ObjectId
from dotenv import load_dotenv
import json
import pymongo
import os
import sys

app = Flask(__name__)

if sys.argv[1] == 'DEV':
    load_dotenv()

MONGO_DB_URI = os.environ.get('MONGO_DB_URI')

print('mongo_db_uri', MONGO_DB_URI)
print('port', os.environ.get('PORT'))

client = pymongo.MongoClient(MONGO_DB_URI)

db = client[os.environ.get('MONGO_DB_NAME')]

@app.route('/api/v1/stores', methods = ['GET'])
def stores():
    try:
        all_stores = db.stores.find()
    except:
        return Response(json.dumps({'error_message': 'Error while consulting the database'}), mimetype='application/json')
    json_stores = list(map(lambda store: {**store, '_id': str(store['_id'])}, all_stores))
    return Response(json.dumps({'all_stores': json_stores}), mimetype='application/json')

@app.route('/api/v1/stores/add', methods = ['POST'])
def add_store():
    
    data = request.get_json()
    
    if not data:
        return Response(json.dumps({'error_message': 'Invalid json data'}))
    
    new_store_data = data.get('new_store')

    try:
        db.stores.insert_one(new_store_data)
    except:
        return Response(json.dumps({'error_message': 'Error while inserting the document in the database'}), mimetype='application/json')

    return Response(json.dumps({'success': True, 'error_message': None}))

@app.route('/api/v1/stores/update/<store_id>', methods = ['PUT'])
def update_store(store_id):
    
    if not store_id:
        return Response(json.dumps({'error_message': 'Not id provided'}), mimetype='application/json')

    data = request.get_json()
    if not data:
        return Response(json.dumps({'error_message': 'Invalid json data'}), mimetype='application/json')
    
    try:
        db.stores.update_one({'_id': ObjectId(store_id)}, {'$set': data['new_store_data']})
    except:
        return Response(json.dumps({'error_message': 'Error while updating the database'}), mimetype='application/json')

    return Response(json.dumps({'success': True, 'error_message': None}), mimetype='application/json')

@app.route('/api/v1/stores/delete/<store_id>', methods = ['DELETE'])
def delete_store(store_id):

    if not store_id:
        return Response(json.dumps({'error_message': 'Not id provided'}), mimetype='application/json')
    
    try:
        db.stores.delete_one({'_id': ObjectId(store_id)})
    except:
        return Response(json.dumps({'error_message':'Error while deleting document'}))
    
    return Response(json.dumps({'success': True, 'error_message': None}))

if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get('PORT', 5000))
    serve(app, host='0.0.0.0', port=port, ident='debug')