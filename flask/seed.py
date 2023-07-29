import random
import string
import hashlib
import secrets
from sqlalchemy import func  # Import the 'func' object
from faker import Faker
from newsfeed_shoppingcart.src.models import Account, User, Admin, Order, Category, db
from newsfeed_shoppingcart.src import create_app

USER_COUNT = 50
ADMIN_COUNT = 50
ACCOUNT_COUNT =50
ORDER_COUNT = 100
CATEGORY_COUNT = 200
LIKE_COUNT = 400

def random_passhash():
    # Get hashed and salted password of length N | 8 <= N <= 15
    raw = ''.join(random.choices(
        string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
        k=random.randint(8, 15)  # length of pw
    ))
    salt = secrets.token_hex(16)
    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()

def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(Account.__table__.delete())
    db.session.execute(User.__table__.delete())
    db.session.execute(Admin.__table__.delete())
    db.session.execute(Order.__table__.delete())
    db.session.execute(Category.__table__.delete())
    db.session.commit()



def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

     # Insert accounts into 'accounts' table
    for _ in range(ACCOUNT_COUNT):
        account = Account(
            username=fake.unique.first_name().lower() + str(random.randint(1, 150)),
            password=random_passhash(),
        )
        db.session.add(account)
    db.session.commit()

    # Insert admin into 'admins' table
    for _ in range(ADMIN_COUNT):
        admin = Admin(
            user_name=fake.unique.first_name().lower() + str(random.randint(1, 150)),
            password=random_passhash(),
            
            account=db.session.query(Account).order_by(func.random()).first()  # Get a random Account for the admin
        )
        db.session.add(admin)
    db.session.commit()
    
    # Insert users into the 'users' table
    for _ in range(USER_COUNT):
        user = User(
           user_name=fake.unique.first_name().lower() + str(random.randint(1, 150)),
           date_of_birth=fake.date_of_birth(),
           email=fake.unique.email(),
           password=random_passhash(),
           address=fake.address(),
           account=db.session.query(Account).order_by(func.random()).first()  # Get a random Account for the user
        )
    db.session.commit()

    # Insert orders into the 'orders' table
    for _ in range(ORDER_COUNT):
        order = Order(
            quantity=random.randint(1, 10),
            discount=random.uniform(0, 100),
            status=fake.word(),
            price=random.uniform(10, 1000),
            created_at=fake.date_time_this_year(),
            user_id=random.randint(1, USER_COUNT)  # Assuming user ids start from 1
        )
        db.session.add(order)
    db.session.commit()

    # Insert categories into the 'categories' table
    for _ in range(CATEGORY_COUNT):
        category = Category(
            product_name=fake.unique.word(),
            description=fake.sentence(),
            price=random.uniform(10, 500),
            #picture=fake.image_url(),
            user_id=random.randint(1, USER_COUNT)  # Assuming user ids start from 1
        )
        db.session.add(category)
    db.session.commit()

# Run script
main()
