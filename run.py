from flask import Flask
from app import create_app

app = create_app()


app.debug = True
if __name__ == '__main__':
	app.run()
