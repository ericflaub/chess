import berserk
import datetime
from datetime import date
import knowledge

account = knowledge.account()
session = berserk.TokenSession(account.token)
client = berserk.Client(session=session)

eric = client.account.get()
start_date = eric['createdAt']
end_date = date.today()

client.games.export_by_player('icererci', since=start_date, until=end_date)
games = list(_)
error_count = []
outcome_series = []
for i in games:
    a = i
    if a['rated'] == True:
        try:
            w_player = a['players']['white']['user']['name']
            b_player = a['players']['black']['user']['name']
            w_change = a['players']['white']['ratingDiff']
            b_change = a['players']['black']['ratingDiff']


            if (w_player == 'icererci' and w_change > 0) or (b_player == 'icererci' and b_change > 0):
                outcome = 1
            elif (w_player == 'icererci' and w_change == 0) or (b_player == 'icererci' and b_change == 0):
                outcome = 3
            else:
                outcome = 0
            outcome_series.append(outcome)
        except:
            error_count.append('oh no')
            pass
len(outcome_series)
error_count