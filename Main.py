from flask import Flask, render_template
from Files import Files
from Multilist import LinkedList
app=Flask(__name__)
@app.route('/')
def root():
   markers=[
   {
   'lat':10.977961,
   'lon':-74.815546,
   'popup':'This is Barranquilla.'
    }
   ]
   return render_template('index.html',markers=markers )
if __name__ == '__main__':
   paises = LinkedList()
   f = Files()
   app.run(host="localhost", port=8080, debug=True)