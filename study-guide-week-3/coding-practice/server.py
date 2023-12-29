"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

@app.route('/save-name', methods=["POST"])
def save_name():
    """save name"""
    name = request.form.get('name')
    session['name'] = name

    return redirect('/')

@app.route('/results')
def show_results():
    """Show resulting message."""
    cheery = request.args.get('cheery')
    dreary = request.args.get('dreary')
    honest = request.args.get('honest')
    message = ''
    if cheery:
        message+='Cheery: The glass if half full. '
    if dreary: 
        message+='Dreary: The glass is almost empty. '
    if honest:
        message+="Honest: Does not matter how full glass of water is, we have 30 gallons more."

    return render_template('results.html', message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

