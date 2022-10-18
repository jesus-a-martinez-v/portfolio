import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            _write_to_csv(data)

            return redirect('thankyou.html')
        except:
            return "Couldn't save to database."

    return 'something went wrong'


def _write_to_csv(data):
    with open('database.csv', 'a') as file:
        csv_writer = csv.DictWriter(file,
                                    fieldnames=['email', 'subject', 'message'],
                                    delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)


if __name__ == '__main__':
    app.run()
