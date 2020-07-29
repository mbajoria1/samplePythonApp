from flask import Flask
from activity import student_favorite


application = Flask(__name__)

application.register_blueprint(student_favorite, url_prefix='/favoriteContent')

@application.route('/')
def index():
	return 'hello world'


if __name__ == '__main__':
	application.run()
