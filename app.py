from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

# need to be underneath app because it relies on app being defined.
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
  prompts = story.prompts
  # print("prompts:")
  # print(prompts)
  return render_template("homepage.html", prompts=prompts)

@app.route("/results")
def showResults():
  generatedStory = story.generate(request.args)

  return render_template("results.html", generatedStory=generatedStory)