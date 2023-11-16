from flask import Flask, render_template, redirect

app = Flask(__name__)
basket = {}

@app.route('/')
def root():
    total_price = sum([2.0 for _ in basket])
    return render_template('Home.html', basket=basket)

@app.route('/add_to_basket/<item>', methods=['POST'])
def add_to_basket(item):
    if item in basket:
        basket[item] += 1
    else:
        basket[item] = 1
    return redirect('/shop')

@app.route('/remove_from_basket/<item>', methods=['POST'], endpoint='remove_from_basket')
def remove_from_basket(item):
            if item in basket:
                basket[item] -= 1
                if basket[item] == 0:
                    del basket[item]
                return redirect('/shop')

@app.route('/caves', endpoint='caves')
def caves():
        return render_template('caves.html')


@app.route('/shop', endpoint='shop')
def shop():
        return render_template('shop.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
