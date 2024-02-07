# Fiberz

# Calculating MX Dye
# Feb 5 2024
# Author: Ellie

# Purpose: Writing code to calculate the math so I don't have to

#Dry Weight of Goods/ Weight of Fiber
DWG = float (input ('Enter Dry Weight of Goods (grams): \n'))
#print ('DWG: ', DWG)

# Depth of Dye
DOD = float (input ('Enter Depth of Dye (percentage): \n'))
DOD = DOD / 100
#print ('DOD: ', DOD)

# Water
water = (DWG * 20)/1000
#print ('Water:', water, ' liters')

# Salt
if DOD >= 0.05:
    salt = (water * 65)
else: salt = (water * 45)
#print ('Salt: ', salt, 'grams')

# Amount of Dye
dye = (DOD * DWG)/0.01
#print ('Dye: ', dye, 'ml')

# Soda Ash
if DOD >= 0.06 :
    soda_ash = water * 14
if DOD < 0.06 and DOD > 0.02:
    soda_ash = water * 10
if DOD <=0.02:
    soda_ash = water * 4
#print ('Soda Ash: ', soda_ash, 'grams')

#values
print ('DWG: ', DWG, 'grams')
print ('DOD: ', round((DOD *100),2), '%')
print ('Water:', water, 'l')
print ('Salt: ', salt, 'grams')
print ('Dye: ', round (dye,2), 'ml')
print ('Soda Ash: ', soda_ash, 'grams')
