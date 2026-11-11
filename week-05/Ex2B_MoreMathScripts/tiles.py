import math  

length = float(input("Enter the room length in feet: "))
width = float(input("Enter the room width in feet: "))

Area = length * width 

boxes_needed = math.ceil(Area /12)
total_boxes = math.ceil(( Area * 1.10) / 12)

print(f"You need {boxes_needed} boxes of tiles.")
print(f"With 10% extra, you need to buy {total_boxes} boxes.")



