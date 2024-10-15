import random

pai_list=['♥2','♠2','♦2','♣2','♥3','♠3','♦3','♣3',
          '♥4','♠4','♦4','♣4','♥5','♠5','♦5','♣5',
          '♥6','♠6','♦6','♣6','♥7','♠7','♦7','♣7',
          '♥8','♠8','♦8','♣8','♥9','♠9','♦9','♣9',
          '♥10','♠10','♦10','♣10',
          '♥A','♠A','♦A','♣A','♥K','♠K','♦K','♣K',
          '♥J','♠J','♦J','♣J','♥Q','♠Q','♦Q','♣Q',
          'JOKER','joker']
pai_liu = []
pai_zhang = []
pai_guo = []
index=[]
pai=[]
for i in range(len(pai_list)):
    index.append(i)
random.shuffle(index)

for data in index:
    pai_data=[]
    pai_data.append(pai_list[data])

pai_liu=pai_data[0:17]
pai_zhang=pai_data[17:34]
pai_guo=pai_data[34:51]
print(pai_liu)
print(pai_zhang)
print(pai_guo)