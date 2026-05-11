from flask import Flask, render_template
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
   app.run(host="localhost", port=8080, debug=True)