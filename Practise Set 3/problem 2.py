from itertools import count
from turtle import st


Story = "my Name is Zubair Rasheed. I've done my MSc in Mathematics from UoK"

print(len(Story))
print(Story.endswith("UoK")) #only find last alphabet of the paragraph
print(Story.count("m")) #count fn help to find alphabet available in string
print(Story.capitalize()) #capitalize fn only work at first word
print(Story.upper()) #upper fn convert small to capital 
print(Story.lower()) #upper fn convert capital to small
print(Story.find("Rasheed")) #find fn help to find word at exact location with index
print(Story.replace("Rasheed.", "Rasheed,"))
