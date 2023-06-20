from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {
        'name': 'Крокодил Гена',
        'price': 19.99,
        'image': 'gena.jpg'
    },
    {
        'name': 'Product 2',
        'price': 29.99,
        'image': 'tsebu.jpg'
    },
    {
        'name': 'Product 3',
        'price': 39.99,
        'image': 'sipsik.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
