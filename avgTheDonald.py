import json
import string


def averageEmotions():
    with open('cashTheseHands.json') as json_data:
        d = json.load(json_data)
        data = json.dumps(d, indent=1)
        j = json.loads(data)
       
        trump = j['emotion']['targets'][0]['emotion']
        try: 
            donald = j['emotion']['targets'][1]['emotion']
        except:
            donald = trump
        theDonaldEmotions = {'anger': 0.00, 'joy': 0.00, 'sadness':0.00, 'fear':0.00, 'disgust':0.00 }
        
        for emotion in donald:
            sum = 0.00
            avg = 0.00
            sum = donald[emotion] + trump[emotion]
            avg = sum/2
            theDonaldEmotions[emotion] = avg
        print "Current emotions towards the president: ", theDonaldEmotions
    return(theDonaldEmotions)

def publicEmotions():
    with open('cashTheseHands.json') as json_data:
        d = json.load(json_data)
        data = json.dumps(d, indent=1)
        j = json.loads(data)
        
        docEmotions = {'anger': 0.00, 'joy': 0.00, 'sadness':0.00, 'fear':0.00, 'disgust':0.00 }
        docEmo= j['emotion']['document']['emotion']
        print "Current public emotions: ", docEmo
        return(docEmo)

if __name__ == '__main__':
    print averageEmotions()
    print publicEmotions()

