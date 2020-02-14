from flask_frozen import Freezer
from jason_blues_app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    