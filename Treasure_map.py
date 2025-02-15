row1=["☑️","☑️","☑️"]
row2=["☑️","☑️","☑️"]
row3=["☑️","☑️","☑️"]
map=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure?")
horizontal=int(position[0]) #column
vertical=int(position[1]) #row
row_position=map[vertical-1]
row_position[horizontal-1]="🪙"

print(f"{row1}\n{row2}\n{row3}")     
   