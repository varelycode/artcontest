import discord
import discord.ext.commands
import pyrebase
import json

with open('serviceAccountKey.json') as f:
  config = json.load(f)

firebase = pyrebase.initialize_app(config)

db = firebase.database()
storage = firebase.storage()




#storage.child("images/example.jpg").put("example2.jpg")
#db.child("users").child("")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def check_msg(message):

    # result = isinstance(author, str)
    # if result:
    #     print("Yes! given variable is an instance of type string")
    # else:
    #     print("No! given variable is not an instance of type string")
    if message.author == client.user:
        return "Missing" and "missing2"

    if message.content.startswith('-ac h'):
        await message.channel.send('To use artcontest, message the artcontest bot and type the following commands:')
        result = 'To use artcontest, message the artcontest bot and type the following commands:'
        return result and message.content
    if message.content.startswith('-ac simg'):
        channel = message.channel
        await message.channel.send('Attach your image...')

        def check_img(m):
            if m.attachments:
                att = m.attachments
                if att:
                    print("detects att")
                    for a in att:
                        if a.filename.endswith("png") or a.filename.endswith("jpg"):
                            print("valid file. Submitted.")
                            return m.attachments and m.channel == channel
                        else:
                            print("invalid file type")
                else:
                    print("no attachment added. Quit by typoing -artcontest end or add file")
                return m.attachments and m.channel == channel
            else:
                print("no attachements sent pls attach somethin")
        msg = await client.wait_for('message', check=check_img)
        await channel.send('File Submitted: {.attachments[0].url}'.format(msg))
        return msg and message.content
    if message.content.startswith('-ac sdesc'):
        channel = message.channel
        await message.channel.send('Write your description in ONE message...')
        def check_desc(m):
            if m.content:
                return m.content and m.channel == channel
        msg = await client.wait_for('message', check=check_desc)
        await channel.send('Description Submitted: {.content}'.format(msg))
        return msg and message.content
    if message.content.startswith('-ac scredits'):
        channel = message.channel
        def check_creds(m):
            if m.content:
                return m.content and channel == m.channel
        await message.channel.send('Add your credits in ONE message...')
        msg = await client.wait_for('message', check=check_creds)
        await channel.send('Credits Submitted: {.content}'.format(msg))
        return msg and message.content




@client.event
async def on_message(message):
    try:
        msginfo, content = await check_msg(message)
        print('return value on_message')
        print(msginfo)
        print(content)
    except Exception as e:
        print(e)


    # data = {"discord_id": authorid, "name": name, "art_url": url, "creds": creds, "desc": desc}
    # db.child("users").push(data)
with open("discordkey.txt") as f:
    s = f.read()
client.run(s)
