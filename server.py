from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def load_html(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')


@app.route('/form_submit', methods=['POST', 'GET'])
def form_submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    return 'Something wen wrong'
