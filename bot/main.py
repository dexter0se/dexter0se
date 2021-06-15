import discum
import time
# import mysql.connector
# from mysql.connector import Error
# import pandas as pd 

bot = discum.Client(token='mfa.J0nLid8CA537BvsYhB0z9jPKvme3MzcXNIomcsj9PbjqXsOGA_femVXHOhOENWEi2EWEXvEaaPHcvtEK8Xbb', log=False)

bot.sendMessage("845616861981835337", "Damn, I was down. But it feels good to be back! :)")

@bot.gateway.command
def tipCatcher(resp):

    if resp.event.ready_supplemental: #ready_supplemental is sent after ready

        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))

    if resp.event.message:

        msg = resp.parsed.auto()
        
        if (msg['author']['id'] == "617037497574359050") and ("title" in msg['embeds'][0].keys()):

            if 'An airdrop appears' in msg['embeds'][0]['title']:

                try:
                    value = msg['embeds'][0]['description'].split('\xa0')[1].split(')')[0]
                except:
                    value = "$0"

                reaction = msg['embeds'][0]['description'].split('\n\nReact with ')[1].split(' to collect it up before it disappears!')[0]

                time.sleep(2)

                if(float(value.split('$')[1]) >= 0.01) and (msg['channel_id'] != "617048119426678930"):

                    bot.addReaction(msg['channel_id'],msg['id'],reaction)

bot.gateway.run(auto_reconnect=True)
