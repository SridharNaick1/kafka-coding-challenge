# import statements
import random
import time 

# set of userIds for random messages
user_id = ['j12345678', 'j87654321', 'j11223344', 'j44332211'] 

# function to create message payload
def get_payload():
    return {
        "userId":random.choice(user_id),
        "visitorId":"jas8v98171",
        "type":"Event",
        "metadata":{
        "messageId":"123sfdafas-32487239857dsh98234",
        "sentAt":int(time.time()),
        "timestamp":int(time.time()),
        "receivedAt":0,
        "apiKey":"apikey1",
        "spaceId":"space1",
        "version":"v1"
        },
        "event":"Played Movie",
        "eventData":{
        "MovieID":"MIM4ddd4"
        }
    }


if __name__ == "__main__":
    get_payload()