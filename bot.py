import praw

id = "ArLPuimfx6-kw3tqB_eunA"
secret = "qq9XD24-L7YKmbT8ocRYKnhSlnkraQ"
username = "new-response-bot"
password = "Ksj011012!!!"
UA = "New Response Just Dropped by u/washuthrowaway123"

reddit = praw.Reddit(
    client_id = id,
    client_secret = secret,
    username = username,
    password = password,
    user_agent = UA
)

subreddit = reddit.subreddit("AnarchyChess")
selfAuthor = set()
alreadyRepliedTo = set()

# new load has to be in delicates
for comment in subreddit.stream.comments(skip_existing=True):
    body = comment.body.lower()
    if "new response" in body and comment.author not in selfAuthor and comment.id not in alreadyRepliedTo:
        newComment = comment.reply("Stop saying \"New response just dropped?\" every time someone says something on this godforsaken sub, no, a new response did not drop, just an average mediocre statement that adds nothing more to a conversation, for the love of fucking god.")
        selfAuthor.add(newComment.author)
        print(f"replying to {comment.id}")
        alreadyRepliedTo.add(comment.id)
