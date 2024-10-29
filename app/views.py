from app import app, db
from flask import render_template, url_for, redirect, flash
from flask import request, session, jsonify
from .forms import RegistrationForm, ProductForm
from .models import User, Product, Order, OrderItem, Stock, Review
from werkzeug.utils import secure_filename
import os
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from sqlalchemy import or_
UPLOAD_FOLDER = 'app/static/images/'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    cart = session.get('cart', {})
    top_rated_products = db.session.query(
        Product.id,
        Product.name,
        Product.description,
        Product.image_filename,
        Product.price,
        db.func.avg(Review.rating).label('average_rating')
    ).join(Review).group_by(Product).order_by(db.desc(
        'average_rating')).limit(4).all()
    most_sold_products = db.session.query(
        Product.id,
        Product.name,
        Product.description,
        Product.image_filename,
        Product.price,
        db.func.sum(OrderItem.quantity).label('total_quantity_sold')
    ).join(OrderItem).group_by(Product).order_by(
        db.desc('total_quantity_sold')).limit(4).all()
    return render_template('home.html', cart=cart,
                           top_rated_products=top_rated_products,
                           most_sold_products=most_sold_products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process registration logic here (e.g., create user in the database)
        user = User(username=form.username.data,
                    email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def is_admin():
    return (current_user.is_authenticated and current_user.username == 'admin'
            and current_user.password == 'adminPass')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            session['cart'] = user.cart
            if is_admin():
                return redirect(url_for('add_product'))
            else:
                return redirect(url_for('products'))
    return render_template('login.html')


@app.route('/products', methods=['GET'])
def products():
    # Fetch the list of products from the database
    cart = session.get('cart', {})
    products = Product.query.all()
    return render_template('products.html', products=products, cart=cart)


@app.route('/sort_products', methods=['GET'])
def sort_products():
    sort_by = request.args.get('sort_by', 'none')

    if sort_by == 'price_high':
        products = Product.query.order_by(Product.price.desc()).all()
    elif sort_by == 'price_low':
        products = Product.query.order_by(Product.price).all()
    else:
        products = Product.query.all()

    return render_template('products.html', products=products)


@app.route('/filter_products', methods=['GET'])
def filter_products():
    category_filter = request.args.get('category_filter', 'all')
    if category_filter == 'all':
        products = Product.query.all()
    else:
        products = Product.query.filter_by(category=category_filter).all()

    return render_template('products.html', products=products)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('products'))


@app.route('/admin/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if is_admin():
        form = ProductForm()
        products = Product.query.all()
        if (request.method == 'POST' and
                form.validate_on_submit() and form.validate()):
            image = form.image.data
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Create a new product
            new_product = Product(
                name=form.name.data,
                price=form.price.data,
                category=form.category.data,
                description=form.description.data,
                image_filename=filename,
                stock=[Stock(quantity=form.stock.data)]
            )
            # Save the product to the database
            db.session.add(new_product)
            db.session.commit()

            return redirect(url_for('add_product'))

    return render_template('add_product.html',
                           form=form, products=products)
                        


@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        # Update product details based on the form submission
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.description = request.form['description']
        product.category = request.form['category']
        stock = int(request.form['stock'])
        stocks = Stock.query.filter_by(product_id=product.id).first()
        if stocks:
            stocks.quantity = stock
        else:
            stocks = Stock(product_id=product.id, quantity=stock)
            db.session.add(stocks)
        # Commit changes to the database
        db.session.commit()
        # Redirect to the product page after editing
        return redirect(url_for('add_product'))

    # Render the edit product page
    return render_template('add_product.html', product=product)


@app.route('/delete_product/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)

    # Delete the product from the database
    db.session.delete(product)
    db.session.commit()

    # Redirect to the product list page after deleting
    return redirect(url_for('add_product'))


@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    # Redirect to the product list page after deleting
    product_objects = Product.query.all()
    productlist = {str(product.id): product for product in product_objects}
    cart_items = []
    total_cart_amount = 0

    for product_id, quantity in cart.items():
        product = productlist.get(product_id)
        if product:
            subtotal = quantity * product.price
            total_cart_amount += subtotal

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
    return render_template('cart.html', cart=cart,
                           productlist=productlist,
                           total_cart_amount=total_cart_amount)


@app.route('/cart_addition/<int:product_id>', methods=['POST'])
def cart_addition(product_id):
    cart = session.get('cart', {})
    str_product_id = str(product_id)
    cart[str_product_id] = int(cart.get(str_product_id, 0)) + 1
    session['cart'] = cart
    current_user.cart = cart
    db.session.commit()
    return redirect(url_for('products'))


@app.route('/cart_subtraction/<int:product_id>', methods=['POST'])
def cart_subtraction(product_id):
    cart = session.get('cart', {})

    # Check if the product_id is in the cart
    if str(product_id) in cart:
        cart[str(product_id)] -= 1
        if cart[str(product_id)] <= 0:
            del cart[str(product_id)]

        # Update the session with the modified cart
        session['cart'] = cart

        # Update the database with the modified cart
        if current_user.is_authenticated:
            current_user.cart = cart
            db.session.commit()
    return redirect(url_for('cart'))


@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    user = current_user
    new_order = Order(user=user, order_date=datetime.now())
    has_enough_stock = True
    for product_id, quantity in user.cart.items():
        product = Product.query.get(product_id)
        stock = Stock.query.filter_by(product_id=product_id).first()
        if product and stock and stock.quantity >= quantity:
            # If there is enough stock, add the order item
            order_item = OrderItem(
                product=product, quantity=quantity, price=product.price)
            new_order.items.append(order_item)
            stock.quantity -= quantity
        else:
            # If there is not enough stock, set the flag to False
            has_enough_stock = False
            flash(f"Not enough stock for {product.name}.", 'danger')

    # If there is enough stock for all items, proceed with the order
    if has_enough_stock:
        db.session.add(new_order)
        db.session.commit()
        # Empty the user's cart
        user.cart = {}
        session['cart'] = {}
        db.session.commit()

        flash('Order placed successfully!', 'success')
        return redirect(url_for('products'))

    # If there is not enough stock for some items, redirect back to the cart
    return redirect(url_for('cart'))


@app.route('/order')
@login_required
def order():
    orders = Order.query.filter_by(user=current_user).all()
    return render_template('order.html', orders=orders)


@app.route('/rate_product/<int:order_item_id>', methods=['GET', 'POST'])
@login_required
def rate_product(order_item_id):
    order_item = OrderItem.query.get(order_item_id)

    if order_item is None or order_item.order.user != current_user:
        flash('Invalid order item.', 'danger')
        return redirect(url_for('order'))

    if request.method == 'POST':
        rating = int(request.form.get('rating'))
        content = request.form.get('content')

        # Check if the user has already reviewed the product in this order_item
        existing_review = Review.query.filter_by(
            user=current_user, product=order_item.product).first()
        if existing_review:
            flash('You have already reviewed this product.', 'warning')
            return redirect(url_for('order'))

        # Save the review
        review = Review(user=current_user, product=order_item.product,
                        order_item_id=order_item_id,
                        rating=rating, content=content)
        db.session.add(review)
        db.session.commit()

        flash('Review submitted successfully!', 'success')

    return redirect(url_for('order'))


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')

    # Use SQLAlchemy to search for products with names containing the query
    products = Product.query.filter(
        or_(Product.name.ilike(f'%{query}%'))).all()

    # Convert the results to a list of dictionaries
    html_content = render_template('product_cards.html', products=products)

    # Return the results as JSON
    return jsonify({'html': html_content,
                    'products': [{'name': product.name}
                                 for product in products]})
