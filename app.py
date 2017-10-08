from flask import Flask, request, render_template
import random


app = Flask(__name__)

@app.route("/")
def form1():
	return render_template("index.html")
	
	

@app.route("/fact", methods=["POST"])
def form1_post():
	name = request.form["text"]
	with open('facts.txt') as f:
		facts = f.readlines()
		l = len(facts)
	
	randnumber = random.randint(0,l-1)
	fact = facts[randnumber]
	return render_template("fact.html", **locals())
	
	
if __name__ == "__main__":
	app.debug = True
	app.run()