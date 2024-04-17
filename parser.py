from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError

phone = '+11111111111' #НОМЕР ТЕЛЕФОНА
api_id = 0 #ПОЛУЧЕННЫЙ С my.telegram.org API_ID
api_hash = '' #ПОЛУЧЕННЫЙ С my.telegram.org API_HASH

client1 = TelegramClient(phone, api_id, api_hash)
 
client1.connect()
if not client1.is_user_authorized():
    client1.send_code_request(config.phone1)
    client1.sign_in(config.phone1, input('Enter the code for 1 client: '))
  
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client1(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print('Choose a group to scrape members from:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1
 
g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]
 
print('Fetching Members...')
all_participants = []
all_participants = client1.get_participants(target_group, aggressive=True)
 
print('Saving In file...')
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        writer.writerow([username])
print('Members scraped successfully.')