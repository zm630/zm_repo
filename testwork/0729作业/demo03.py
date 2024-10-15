data_str="1, 2, 3, 4, 5, 6"
def zfc(data_str):
  min=1
  for i in data_str:
    if(i != ","):
      if(int(i<min)):
        min=int(i)

  return min
  zfc(data_str)
