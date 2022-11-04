from flask import Flask, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html") #if you want to render a .html file,
                                        # import render_template from flask and use
                                        #render_template("index.html") here.
@app.route('/stories')
def stories():
  return render_template("stories.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")

if __name__ == '__main__':
    app.debug = True
    app.run() #go to http://localhost:5000/ to view the page.