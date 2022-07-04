# How I Built This:

### Flask Mad Libs:

##### Setting Up Flask App:

1. In Terminal:
```console
git init
```

2. In Terminal:
```console
touch .gitignore
```

3. In Terminal:
```console
python3 -m venv venv
```

4. In Terminal:
```console
source venv/bin/activate
```

5. In Terminal, 
```console
pip3 install flask
```

6. In Terminal:
```console
pip3 freeze > requirements.txt
```

7. Add venv folder to .gitignore
In .gitignore, add venv/

8. In Terminal:
```console
touch app.py
```

9. In Terminal:
```console
FLASK_ENV=development flask run

Error: Failed to find Flask application or factory in module 'app'. Use 'FLASK_APP=app:name' to specify one.
```

##### Build out app.py:

10. Get basic Flask App Working:
Inside app.py
```python
from flask import Flask

app = Flask(__name__)
```

11. Run flask app:
```console
FLASK_ENV=development flask run
```
Flask app should be running now without errors, but text should say:
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.

##### Install Debugger Tool:

12. Inside Terminal:
```console
pip3 install flask-debugtoolbar
```

13. Updating requirements.txt file:
```console
pip3 freeze > requirements.txt
```

14. Inside app.py:
```python
from flask_debugtoolbar import DebugToolbarExtension

# need to be underneath app because it relies on app being defined.
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)
```

15. Create a homepage route with a body element for the HTML
```python
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# need to be underneath app because it relies on app being defined.
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
  return """
  <body>
    <p>Hello World</p>
  </body>
  """
```
Debug toolbar should now be available.

##### Build Out Homepage

16. Inside app.py, let's create the landing/homepage:
```python
from flask import Flask, request, render_template
from stories import story

@app.route("/")
def homepage():
  """Generate form and ask for words"""
  prompts = story.prompts
  # print("prompts:")
  # print(prompts)
  return render_template("homepage.html")
```

17. Create a templates folder:
Create a file named homepage.html
```html
<!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <p>Here</p>
</body>
</html>
```

18. Build out the homepage.html:
Start with the form:
```html
<!doctype html>
<html>
<head>
  <title>Madlibs</title>
</head>
<body>
  <h1>Madlibs</h1>
  <!-- Not sending the data anywhere yet -->
  <form action="">
    {% for prompt in prompts %}
    <p>{{prompt}}:
      <input name="{{ prompt }}">
    </p>
    {% endfor %}
    <button>Submit</button>
  </form>
  
</body>
</html>
```

19. Inside app.py:

```python
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
```

20. Currently, form action is not sending the input data anywhere yet.
I'm going to make a results.html file in the templates and create another route to results.html in app.py
```python

```