from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def app():
    return render_template('Home.html')

@app.route('/caves', endpoint='caves')
def caves():
    return render_template('caves.html')


@app.route('/shop', endpoint='shop')
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

