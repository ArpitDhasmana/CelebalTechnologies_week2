from flask import Flask, render_template, request, redirect, flash
from linkedlist import LinkedList

app = Flask(__name__)
app.secret_key = 'supersecretkey'

ll = LinkedList()

@app.route('/')
def index():
    return render_template(
        'index.html',
        nodes=ll.to_list(),
        length=ll.length()
    )

@app.route('/add_end', methods=['POST'])
def add_end():
    data = request.form['data']
    ll.add_end(data)
    flash(f"Added '{data}' at the end.")
    return redirect('/')

@app.route('/add_at', methods=['POST'])
def add_at():
    try:
        data = request.form['data']
        pos = int(request.form['position'])
        ll.add_at(pos, data)
        flash(f"Added '{data}' at position {pos}.")
    except Exception as e:
        flash(str(e))
    return redirect('/')

@app.route('/delete_nth', methods=['POST'])
def delete_nth():
    try:
        pos = int(request.form['position'])
        ll.delete_nth(pos)
        flash(f"Deleted node at position {pos}.")
    except Exception as e:
        flash(str(e))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
