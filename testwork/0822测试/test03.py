file = open("config.txt","w",encoding="utf-8")
file.write("As the New Year has passed away, I think the cold weather will pass away and gets warm soon, but I am wrong. This morning, it snows again and I have to wear a lot of clothes. I guess this is the last snow and the summer is coming soon. I miss summer. I can swim and play with my friends in summer.")
count=0
with open("config.txt","r",encoding="utf-8") as file:
    result=file.readline()
    for data in result:
        if data.isupper()==True:
            count+=1
    print(count)