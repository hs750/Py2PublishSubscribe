from com.harrison.pubsub.PubSubInterface import PubSubInterface


class PubSubImpl(PubSubInterface):
    def __init__(self, name):
        super(PubSubImpl, self).__init__()
        self.name = name

    def receive(self, data):
        print("%s received %s" % (self.name, data))

