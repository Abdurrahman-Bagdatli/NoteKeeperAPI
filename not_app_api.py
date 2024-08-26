from flask import Flask ,request,jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)

CORS(app)

def get_db_Connection(): 
    return pymysql.connect(
    host="localhost",
    user="root",
    password="Abdr20087434",
    database="notedatabase",
)

@app.route("/addItems",methods=["POST"])
def add_Database():
   connection = get_db_Connection()
   cursor = connection.cursor()
   try:
      data=request.json
      items=data.get("items")
      sql = "INSERT INTO notes (Title,Description,Date) values (%s,%s,%s)"
      cursor.execute(sql,(items["Title"],items["Description"],items["Date"],))
      connection.commit()
      return jsonify({"message": "Items added successfully!"}), 201
   finally:  
   
     cursor.close()
     connection.close()


@app.route("/getItems", methods=["GET"])
def get_Database():
    connection = get_db_Connection()
    cursor = connection.cursor()
    try:
        sql = "SELECT * FROM notes;"
        cursor.execute(sql)
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        items = [dict(zip(columns, row)) for row in rows]
        return jsonify(items)
    finally:
        cursor.close()
        connection.close()

        
@app.route("/patchItems",methods=["PATCH"])
def patch_Database():
    connection = get_db_Connection()
    cursor = connection.cursor()
    try:
        data=request.json
        items = data.get("items")
        sql= "UPDATE notes SET Title = %s ,Description = %s,Date= %s WHERE id= %s "
        cursor.execute(sql,(items["Title"],items["Description"],items["Date"],items["id"],))
        connection.commit()
        return jsonify({"message": "Items updated successfully!"}), 200
    finally:
        cursor.close()
        connection.close()


@app.route("/deleteItems",methods=["DELETE"])
def remove_Database():
    connection = get_db_Connection()
    cursor= connection.cursor()
    try:
        data = request.get_json()
        items= data.get("id")
        sql="DELETE from notes where id=%s"
        cursor.execute(sql,(items))
        connection.commit()
        return jsonify({"message":"Items remove successfully!"})
    finally:
        cursor.close()
        connection.close()




if __name__ == "__main__":
    app.run( host="0.0.0.0",port=5000,debug=True)