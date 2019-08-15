from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1155925772973928448-uhQ0XqPtUN36G4q1m0mZOjjVpw0CS3"
access_token_secret = "J0OyFHOfHbduGoGVGlC4BkDafYHJeSJLntpZiayhvAyJw"
consumer_key = "aYuVbpNpaeKaNm4wLwKkdcPqC"
consumer_secret = "AlrNBDNWv0GMt15uDDHU36flRdpV13Mmmu6qlS9qmEzi5DmthK"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
