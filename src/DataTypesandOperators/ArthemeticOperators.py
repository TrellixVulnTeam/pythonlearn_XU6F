# + Addition
# - Subtraction
# * Multiplication
# / Division
# % Mod (the remainder after dividing)
# ** Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
# // Divides and rounds down to the nearest integer


#
# 1.My electricity bills for the last three months have been $23, $32 and $64.
# What is the average monthly electricity bill over the three month period?
# Write an expression to calculate the mean, and use print() to view the result.



# Write an expression that calculates the average of 23, 32 and 64
month1=23
month2=32
month3=64

# Place the expression in this print statement
def averagebill(month1,month2,month3):
    return (month1 + month2 + month3) / 3

print("Average current bill foir three months = ",averagebill(month1,month2,month3))



# 2.In this quiz you're going to do some calculations for a tiler.
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long,
# the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
#
#     How many tiles are needed?
#     You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
#
def TilesNedded(widthtiles,heignttiles):
    return widthtiles*heignttiles

tilesneeded=0
firstroom=TilesNedded(9,7)
secondroom=TilesNedded(5,7)
tilesneeded=firstroom+secondroom
print("Tiles needed for first room = %d and second room = %d and total tiles required is = %d"%(firstroom,secondroom,tilesneeded))

leftovertiles=(17*6)-tilesneeded
print("the tiles will be ledtover after using 17 packges of each containing six tiles is = %d"%(leftovertiles))