#!C:\Python\python.exe
import cgi
import mysql.connector
 #step-1 connect python
print("Content-Type:text/html\n")
print("<html>")
print("<body>")
print("<h1>Welcome to connectivity..</h1>")

#step-2 front to back end
data=cgi.FieldStorage()
Name=data.getvalue("name")
Email=data.getvalue("mail")
phone=data.getvalue("number")
Vareity=data.getvalue("vareities")
Quantity=data.getvalue("sizes")
Address=data.getvalue("address")
Pincode=data.getvalue("pincode")
Payment=data.getvalue("payment")
print("<h1>",Name,Email,phone,Vareity,Quantity,Address,Pincode,Payment,"</h1>")

#step-3 backend to database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coffeeshop"
)
cursordata=db.cursor()
sql="INSERT INTO shopdatabase(Name,Email,phone,Vareity,Quantity,Address,Pincode,Payment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
value=(Name,Email,phone,Vareity,Quantity,Address,Pincode,Payment)
cursordata.execute(sql,value)
db.commit() 
print("</body>")
print("</html>")

