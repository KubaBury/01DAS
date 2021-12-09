import pandas as pd

def like(name, id):
    data = {}
    data.setdefault('user', [])
    data.setdefault('zprava_id', [])
    data['user'].append(name)
    data['zprava_id'].append(id)
    df = pd.DataFrame(data)
    df.to_csv('../data/likes_posted.csv',index=False, header=False, mode='a')

like("vajco", 145)
