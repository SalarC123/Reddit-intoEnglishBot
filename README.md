# intoEnglishBot

## How to use intoEnglishBot

Call the bot by replying `!intoEnglishBot` (letter case does not matter) to any comment in a different language

**intoEnglishBot** will not run 24/7, so include your own information in the code below and run the code on your own device:

```
praw.Reddit(client_id = 'PUT_CLIENT_ID_HERE',
            client_secret = 'PUT_CLIENT_SECRET_HERE',
            password = 'PUT_PASSWORD_HERE',
            user_agent = 'PUT_USER_AGENT_HERE',
            username = 'PUT_USER_NAME_HERE')
```

However, you will need to `pip3 install praw` in your terminal first and remove the line with `from botsecretscopy import...`

Go to [this website](https://www.reddit.com/prefs/apps/) and make a reddit developer application to receive the *client_id* and *secret_id*

`username` and `password` are of your account so don't share the code with these still included

`user_agent` is a string of anything that you would like to refer to the bot as. **For example --> 'intoEnglishBot:v1.1 by u/1Test2Bot3'**


## Contact me

On reddit, private message me on this account:

***1Test2Bot3***
