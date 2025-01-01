import requests
from ranktier import Rank


class Player:
    def __init__(self, userid):
        self.info = requests.get(f'https://api.opendota.com/api/players/{userid}').json()
        self.wl = requests.get(f'https://api.opendota.com/api/players/{userid}/wl').json()
        self.wordcloud = requests.get(f'https://api.opendota.com/api/players/{userid}/wordcloud').json()
        self.herolist = requests.get('https://api.opendota.com/api/heroes').json
        self.playerheroes = requests.get(f'https://api.opendota.com/api/players/{userid}/heroes').json()
        self.matches = requests.get(f'https://api.opendota.com/api/players/{userid}/matches').json

    def heroid(self):
        res = {}
        for i in self.herolist():
            res[i['id']] = i['localized_name']
        return res

    def isvalid(self):
        try:
            if self.info['error'] == 'Not Found':
                return False
        except:
            return True

    def isvalid_wl(self):
        try:
            if self.info['error'] == 'Not Found':
                return False
        except:
            return True

    def personaname(self):
        return self.info['profile']['personaname'] if self.isvalid() else '-'

    def avatarfull(self):
        return self.info['profile']['avatarfull'] if self.isvalid() else '-'

    def profileurl(self):
        return self.info['profile']['profileurl'] if self.isvalid() else '-'

    def plus(self):
        if self.isvalid() == False:
            return '-'
        if self.info['profile']['plus'] == False:
            return 'No'
        else:
            return 'Yes'

    def rank(self):
        try:
            return Rank(self.info['rank_tier'])
        except:
            return '-'

    def winrate(self):
        return round(int(self.wl['win'])/(int(self.wl['win'])+int(self.wl['lose']))*100, 1) if self.isvalid_wl() else '-'

    def win(self):
        return self.wl['win'] if self.isvalid_wl() else '-'

    def lose(self):
        return self.wl['lose'] if self.isvalid_wl() else '-'

    def loccountrycode(self):
        return self.info['profile']['loccountrycode'] if self.isvalid() else '-'

    def wordcloudinfo(self):
        return dict(reversed(list({k: v for k, v in sorted(self.wordcloud['my_word_counts'].items(), key=lambda item: item[1])}.items()))) if self.isvalid() else {'error':'error'}

    def listheroes(self):
        return self.playerheroes if self.isvalid() else '-'

    def last_matches(self):
        try:
            arr = []
            for match in self.matches():
                if len(arr) > 19:
                    return arr
                arr.append([match['match_id'], match['kills'], match['deaths'], match['assists'], self.heroid()[match['hero_id']]])
            return arr
        except:
            return '-'
