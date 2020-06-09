#Exercise!
# Display the image below to the right hand side where
# the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for tempList in picture:
  newstr = ''
  for item in tempList:
    if item == 0:
      newstr += ' '
    elif item == 1:
      newstr += '*'
  print(newstr)
  
