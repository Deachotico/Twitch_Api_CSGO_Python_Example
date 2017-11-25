# CSGOTwitchWatcher
Python script that uses Twitch API to find all streams of CS GO and send a notification by email if there is some stream with more than 20000 watching it.

To use it you need to generate a Client-ID, tutorial is in https://dev.twitch.tv/get-started
Put it in the code here:
  eq.add_header("Client-ID","PUT_IT_HERE")

To use it with other games you can change the parameters sent in the url with other games or options, reference here: https://dev.twitch.tv/docs/v5/reference/streams

Your gmail personal password will not work.
To send the email using a Gmail Account you need a app password, tutorial to generate one is in here:
https://support.google.com/accounts/answer/185833?hl=en
