from flask import Flask, render_template, url_for



app = Flask(__name__)

global total_price
basket = []
total_price = 0
@app.route('/')
def root():
    total_price = sum(item[1] for item in basket)
    return render_template('Home.html', basket=basket, total_price=total_price)

@app.route('/add_to_basket/<item>/<float:price>', methods=['POST'])
def add_to_basket(item,price):
    global total_price
    price = float(price)
    basket.append((item, price))
    total_price = sum(item[1] for item in basket)
   
   


    return render_template('shop.html', basket=basket, total_price=total_price)



@app.route('/remove_from_basket/<item>', methods=['POST'], endpoint='remove_from_basket')
def remove_from_basket(item):
    global basket
    for i, (basket_item,_) in enumerate(basket):
        if basket_item == item:
            del basket[i]
            break

    total_price = 0 if not basket else sum(item[1] for item in basket)
            
       
    return render_template('shop.html',total_price=total_price, basket=basket or [])

@app.route('/caves', endpoint='caves')
def caves():
        return render_template('caves.html')

@app.route('/form', endpoint='forms')
def forms():
    return render_template('form.html')

@app.route('/king', endpoint='king')
def kings():
    return render_template('kingCave.html')

@app.route('/wem', endpoint='wem')
def wemCave():
        return render_template('wemCave.html')


@app.route('/shop', endpoint='shop')
def shop():
   

    return render_template('shop.html')
@app.route('/remove', methods=['POST'])
def remove_basket():
    basket.clear()
    return render_template('shop.html', basket=basket, total_price=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
