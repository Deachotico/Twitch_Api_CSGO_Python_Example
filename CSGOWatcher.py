import urllib.request
import logging
import os 
import json
import email.utils
from emailmodule import send_email

def CSGOWatcher(game=0, viewers=1000, limit=3, email=False):
    #Request to Twitch, receives a json
    gamelist= ['Counter-Strike%3A%20Global%20Offensive','League%20of%20Legends','Fortnite','PLAYERUNKNOWN%27S%20BATTLEGROUNDS', 'Dota%202', 'Overwatch', 'Hearthstone','FIFA%2018' ]
    try:
        if game == 8:
            url = 'https://api.twitch.tv/kraken/streams/?limit=5'
        else:
            url = 'https://api.twitch.tv/kraken/streams/?game={0}&limit={1}'.format(gamelist[game], limit)
        print("URL: ", url)
        req = urllib.request.Request(url)
        #Add YOUR twitch api key to the request
        req.add_header("Client-ID", "PUT_YOUR_ID_HERE")
        resp = urllib.request.urlopen(req)
        data = resp.read()
    except:
        quit()
    #Formatting the string to transform in a dict
    data = str(data)
    data = data.replace("b'{", "{")
    data = data.replace("}}'", "}}")
    data = data.replace("\''", "}}")

    #Set defaults needed and transform the response in a dict
    false = False,
    true = True
    null = None
    response = eval(data)

    #Read and Filter the streams
    arraystreams = []
    for streams in response['streams']:
        #Build the body with all streams over specified viewers watching
        if (streams['viewers'] > viewers):
            email_body = ''
            email_body = email_body+"Stream: "+streams['channel']['status']+'\n'
            email_body = email_body+"Channel: "+streams['channel']['display_name']+'\n'
            email_body = email_body+"Viewers: "+str(streams['viewers'])+'\n'
            # email_body = email_body+"Game:\n"+streams['channel']['game']+'\n'
            email_body = email_body+"Link: "+streams['channel']['url']+'\n\n\n'
            arraystreams.append(email_body)
    #if we have a interesting stream, return streams
    if (arraystreams):
        # if email:
        #     body =''
        #     for stream in arraystreams:
        #         body = body+stream
        #         print(body)
        #     send_email('put_youremail_here' ,'Put your app password here', ['put your destination emails here'],
        #               'CSGO New Livestreams at Twitch', body)
        return arraystreams
    else:
        return ["No interesting streams right now"]