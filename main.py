from flask import Flask, render_template
from app.playerinfo import Player

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:userid>/')
def userinfo(userid):
    player = Player(userid)
    isvalid = player.isvalid()
    personaname = player.personaname()
    avatarfull = player.avatarfull()
    profileurl = player.profileurl()
    plus = player.plus()
    rank = player.rank()
    winrate = player.winrate()
    win = player.win()
    lose = player.lose()
    loccountrycode = player.loccountrycode()
    wordcloud = player.wordcloudinfo()
    listheroes = player.listheroes()
    heroid = player.heroid()
    matches = player.last_matches()
    if isvalid:
        return render_template('userinfo.html', matches=matches, isvalid=isvalid, heroid=heroid,listheroes=listheroes, wordcloud=wordcloud, loccountrycode=loccountrycode, win=win, lose=lose, winrate=winrate, rank=rank, plus=plus, profileurl=profileurl, userid=userid, personaname=personaname, avatarfull=avatarfull)
    else:
        return render_template('notfound.html')

if __name__ == '__main__':
    app.run(debug=True)
