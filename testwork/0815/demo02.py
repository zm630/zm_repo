import random
pai_list=['♥2','♠2','♦2','♣2','♥3','♠3','♦3','♣3',
          '♥4','♠4','♦4','♣4','♥5','♠5','♦5','♣5',
          '♥6','♠6','♦6','♣6','♥7','♠7','♦7','♣7',
          '♥8','♠8','♦8','♣8','♥9','♠9','♦9','♣9',
          '♥10','♠10','♦10','♣10',
          '♥A','♠A','♦A','♣A','♥K','♠K','♦K','♣K',
          '♥J','♠J','♦J','♣J','♥Q','♠Q','♦Q','♣Q',
          'JOKER','joker']
random.shuffle(pai_list)


pai_liu = []
pai_zhang = []
pai_guo = []
for i in range(len(pai_list) - 3):
    if i%3==1:
        pai_liu.append(pai_list[i])
    if i%3==2:
        pai_zhang.append(pai_list[i])
    if i % 3 == 0:
        pai_guo.append(pai_list[i])
print(pai_liu)
print(pai_zhang)
print(pai_guo)
dipai=pai_list[-3:]
print(dipai)
