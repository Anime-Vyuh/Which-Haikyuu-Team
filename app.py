from flask import Flask,url_for,redirect,render_template,request,session,flash
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(16)

team = ['karasuno','nekoma','aoba_jousei','date_tech','ougi_south','inarizaki','shiratorizawa','kamomedai','itachiyama','fukurodani','waku_south','kakugawa','jouzenji','tsubakihara','sarukawa_tech']
@app.route('/',methods=['POST','GET'])
def select():
    if 'username' in session:
        return redirect(url_for('result'))
    if request.method == 'POST':
        uname = request.form['username']
        session['username']= uname
        return redirect(url_for('result'))
    else:
        return render_template('home.html')

@app.route('/selected')
def result():
    if 'username' in session:
        username=session['username']
        haikyuu_team = random.choice(team)
        if '@' in username:
            username,mail = username.split('@')
        flash("Congrats {} you got selected into {}".format(username.capitalize(),haikyuu_team.capitalize().replace('_',' ')))
        return render_template('team.html', name = haikyuu_team, title = 'Haikyuu Team Selection')

if __name__ == '__main__':
    app.run(debug=True)
