from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
     'id': 1,
     'title': 'Data Analysts',
     'location': 'San Francisco, USA',
     'salary': '$200,000'
    },
    {
     'id': 2,
     'title': 'Frontend Engineer',
     'location': 'Philippines',
     'salary': '$190,000'
    },
    {
     'id': 3,
     'title': 'Backend Engineer',
     'location': 'Philippines',
     'salary': '$210,000'
    },
    {
     'id': 4,
     'title': 'Data Scientist',
     'location': 'Tokyo, Japan',
     'salary': '$250,000'
    },
    {
     'id': 5,
     'title': 'Game Developer',
     'location': 'Sydney, Australia',
     'salary': '$200,000'
    },
    {
     'id': 6,
     'title': 'Web Developer',
     'location': 'Remote',
    },
    {
     'id': 7,
     'title': 'Junior Fullstack Developer',
     'location': 'Philippines',
     'salary': '$100,000'
    },
    {
     'id': 8,
     'title': 'System Analysts',
     'location': 'Philippines',
     'salary': '$150,000'
    },
    {
     'id': 9,
     'title': 'Full Stack Developer',
     'location': 'Philippines',
     'salary': '$250,000'
    }
]

@app.route('/')
def hello_kenneth():
    return render_template('home.html',
                           jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)