from flask import Flask, request, jsonify
  

from sql_connection import get_sql_connection
import products_dao  
import uom_dao

connection = get_sql_connection()


app = Flask(__name__) 
 
@app.route('/getProducts')
def get_products():

    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
    
        
  
if __name__ =="__main__":  
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(port=5000)  