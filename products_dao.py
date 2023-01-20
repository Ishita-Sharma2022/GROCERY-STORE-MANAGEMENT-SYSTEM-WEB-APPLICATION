import mysql.connector
from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = ("select products.products_id, products.names, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on uom.uom_id=products.uom_id")

    cursor.execute(query)

    response = []
    for (products_id, names, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'products_id' : products_id,
            'names' : names,
            'uom_id' : uom_id,
            'price_per_unit' : price_per_unit,
            'uom_name' : uom_name
        })    
        
        
   
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products (names, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_names'],product['uom_id'],product['price_per_unit'])
    

    cursor.execute(query, data)
    connection.commit()
    
def delete_product(connection, products_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where products_id=" + str(products_id))
    cursor.execute(query)
    connection.commit()
    
    
    return cursor.lastrowid
    

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12))
    print(delete_product(connection, 10))
    