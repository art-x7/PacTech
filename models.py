from main import db

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prod = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(120), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(120),  nullable=False)

    def __repr__(self):
        return f" Product: {self.prod_name}"