from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    text = request.form.get('note')
    if text:
        notes.append(text)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
