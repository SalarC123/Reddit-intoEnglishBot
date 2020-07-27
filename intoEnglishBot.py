import re
import praw
import goslate
import time
from botsecretscopy import *
from textblob import TextBlob

reddit = praw.Reddit(client_id= PUT_CLIENT_ID_HERE,
                     client_secret= PUT_CLIENT_SECRET_HERE,
                     password= PUT_PASSWORD_HERE,
                     user_agent= PUT_USER_AGENT_HERE,
                     username= PUT_USER_NAME_HERE)

# translator = goslate.Goslate()
# print(translator.translate('Hello world','es'))
# print(translator.detect('Hola mundo'))
# print(translator.get_languages())

# ---- intoEnglishBot ----

def intoEnglishBot():
    for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
        translator = goslate.Goslate()
        try:
            botcall = re.compile('!intoEnglishBot',re.I).search(comment.body).group()
        except AttributeError:
            continue

        try:
            parentcomment = str(reddit.comment(reddit.comment(id=comment.id).parent().id).body)
        except:
            comment.reply('There is no parent comment for me to tranlate!\n\nMake sure to reply to a comment next time or contact the creator "RedditGood123" if there are any issues.')
            continue

        b = TextBlob(parentcomment)
        languagecode = b.detect_language()
        language = translator.get_languages()[str(languagecode)]
        try:
            translation = b.translate(to='en')
        except:
            comment.reply('This text is already in english! Keep in mind that this bot might detect a language to be in english if there are two different languages in the parent comment\n\nIf you think something is wrong, private message the creator at "RedditGood123"')
            continue
        comment.reply(f'I translated the comment from {language.title()} to English\n\n"{translation}"')

intoEnglishBot()
