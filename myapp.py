from flask import Flask, render_template, redirect

app = Flask(__name__)
basket = {}

@app.route('/')
def root():
    total_price = sum([2.0 for _ in basket])
    return render_template('Home.html', basket=basket,)

@app.route('/add_to_basket/<item>/<float:price>', methods=['POST'])
def add_to_basket(item,price):
        basket.append((item,2.0))
        return render_template('shop.html' basket=basket)
            

        total_price = sum([item_dict['price'] * item_dict['quantity'] for item_dict in basket])
        return render_template('Home.html', basket=basket, total_price=total_price)

@app.route('/remove_from_basket/<item>', methods=['POST'], endpoint='remove_from_basket')
def remove_from_basket(item):
    for i, (basket_item,_) in enumerate(basket):
        if basket_item == item:
            del basket[i]
            break
    return render_template('shop.html', basket=basket or [])

@app.route('/caves', endpoint='caves')
def caves():
        return render_template('caves.html')


@app.route('/shop', endpoint='shop')
def shop():
        return render_template('shop.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
