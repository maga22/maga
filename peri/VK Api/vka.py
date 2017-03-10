from urllib.request import urlopen
from json import loads
from time import sleep
from random import choice

friends = []
your_id = '202924573'



data = urlopen('https://api.vk.com/method/friends.get?user_id='+your_id).read().decode('utf-8')
data = loads(data)



#print(data)
friends_id = data['response']



for f_name in friends_id:





#print(friends_id)
for f_id in friends_id:
    data = urlopen('https://api.vk.com/method/friends.get?user_id='+str(f_id)).read().decode('utf-8')
    data = loads(data)
    try:
        friends_friends_id = data['response']
    except:
        continue
    friends.append([f_id,len(set(friends_id) & set(friends_friends_id))])
    sleep(0.2)





friends.sort(key=lambda x: -x[-1])
print(friends)
