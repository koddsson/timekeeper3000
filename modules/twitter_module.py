import twitter


class TwitterModule:
    """
    Posts latest status to twitter given that it differs from the last status.
    """
    def __init__(self):
        self.twitter_client = twitter.Api(
            consumer_key='ZZ1QZXTjbtTByQlRp0fyA',
            consumer_secret='BwBz55dXTuirvm52c11K6oAHYFWibykNAi2tp0oOU',
            access_token_key=
            '1872443180-Y5cf0mkkcjqVEaUpvPf9ETo4nXIpDFIxoOTj69n',
            access_token_secret='fnH1byoAUPxwkgDxseaZGRACcVcFRn53lddFzcc'
        )
        self.last_status = ''

    """
    Activate the module. This is run for every module.
    """
    def activate(self, **kwargs):
        if 'status' in kwargs:
            self.post_to_twitter(kwargs['status'])
            return True
        else:
            return False

    """
    Post the message to twitter unless it is the same as last message.
    """
    def post_to_twitter(self, msg):
        # Twitter API throws a 'Status duplicate' error if this check fails.
        if msg != self.last_status:
            try:
                results = self.twitter_client.PostUpdate(msg)
                if results == msg:
                    self.last_status = msg
            except twitter.TwitterError, e:
                # WTF is this even?
                if e[0][0]['code'] == 187:
                    pass
                else:
                    raise e
