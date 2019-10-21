from flask import render_template
import connexion

#App instance
app = connexion.App(__name__, specification_dir='./')

#Read JSON file
app.add_api("Board_Game_API.json")

#URL route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='localhost', port = 2305, debug = True)
