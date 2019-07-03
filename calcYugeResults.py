
from avgTheDonald import averageEmotions, publicEmotions


theDonaldEmotions = averageEmotions()
publicEmotions = publicEmotions()
def greatestEmotion():
    return max(theDonaldEmotions, key=lambda i: theDonaldEmotions[i])
    
def generalEmotion():
    return max(publicEmotions, key=lambda i: publicEmotions[i])

if __name__== '__main__':
    print greatestEmotion()
    print generalEmotion()
