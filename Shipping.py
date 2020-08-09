'''Sal's Shipping


Sal runs the biggest shipping company in the tri-county area,
Sal’s Shippers. Sal wants to make sure that every single one
of his customers has the best, and most affordable
experience shipping their packages. In this project,
you’ll build a program that will take the weight of
a package and determine the cheapest way to ship
that package using Sal’s Shippers.

Sal’s Shippers has several different options for
a customer to ship their package. They have ground shipping,
which is a small flat charge plus a rate based on the weight
of your package. Premium ground shipping, which is a
much higher flat charge, but you aren’t charged for weight.
They recently also implemented drone shipping, which has
no flat charge, but the rate based on weight is triple
the rate of ground shipping.'''

#Ground Shipping
'''
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

'''

#Drawn Shipping
'''
Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00
'''

#Premium Ground Shipping

#Flat charge: $125.00

#Project goal:
'''
Write a program that asks the user for the weight of their package
and then tells them which method of shipping is cheapest and
how much it will cost to ship their package using Sal’s Shippers.
'''

#Soulution: My programmme: 

def ground_shipping(weight):
    #it will generate the price for ground shipping based on weight 
    flat_charge=20
    if weight<=2:
      rate_charge= 1.50* weight
      return rate_charge + flat_charge
    elif 2<weight<=6:
      rate_charge= 3.00*weight
      return rate_charge + flat_charge
    elif 6<weight<=10:
      rate_charge= 4.00*weight
      return rate_charge + flat_charge 
    else:
       rate_charge= 4.75*weight
    return rate_charge + flat_charge
def drone_shipping(weight):   
    if weight<=2:
      rate_charge= 4.50*weight
      return rate_charge 
    elif 2<weight<=6:
      rate_charge= 9.00*weight
      return rate_charge 
    elif 6<weight<=10:
      rate_charge= 12.00*weight
      return rate_charge 
    else:
      rate_charge= 14.25*weight
      return rate_charge 
def premimum_groundshipping(weight):
    flat_charge= 125
    return flat_charge

def chepeast_price( weight):
    a= ground_shipping(weight)
    b= drone_shipping(weight)
    c= premimum_groundshipping(weight)
    if a<b and a<c:
      print( "Ground shipping is the cheapest way to ship a "+
        str(weight), "pound package. It will cost:","$" + str(a))
    elif b<a and b<c: 
      print( "Drone shipping is  the cheapest way to ship a "+
        str(weight), "pound package. It will cost:","$" + str(b))
    elif c<a and c<b:
      print("Premium Ground Shipping is  the cheapest way to ship a "+
        str(weight), "pound package. It will cost:","$"+ str(c))
    '''elif a==b and a<c:  
      print( "Ground shipping and  Drone_shipping are suitble.",
           "It will cost:" ,"$" + str(a))
    elif a==c and c<b:
      print( "Ground shipping and Premium Ground Shipping are suitble."
           +"It will cost:", "$" + str(a))
    else: 
      print( "All 3 methods are suitble. It will cost:", "$" + str(a))'''
      
#test
'''     
The cheapest way to ship a 4.8 pound package is
using ground shipping and it will cost $34.40.

The cheapest way to ship a 41.5 pound package is
using premium ground shipping and it will cost $125.00. '''

print(chepeast_price(4.8))
print(chepeast_price(41.50))







