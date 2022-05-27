import berserk
import datetime
from datetime import date
import chess_knowledge 
import pandas as pd
import statsmodels.api as sm

account = chess_knowledge.account()
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

# simple model to get the ball rolling. Basically just checking for autoregressive properties of the series
df = pd.DataFrame(outcome_series, columns= ['outcomes'])
df['lag1']=df['outcomes'].shift(1)
df['lag2']=df['outcomes'].shift(2)
df['int'] = 1
df = df.dropna()
X = df[['int','lag1', 'lag2']]
y = df[['outcomes']]
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())


