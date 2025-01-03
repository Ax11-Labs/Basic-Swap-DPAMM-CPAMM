import math

# Global Variables
balanceX = 0
balanceY = 0
priceX = 0
priceY= 0


# set the balance of both tokens
def setBalances(balX, balY):
  global balanceX, balanceY
  balanceX = balX
  balanceY = balY


# set price of X and Y, please fill in the price of X only
def setPrices(priceX_):
  global priceX, priceY
  priceX = priceX_
  priceY = 1/priceX_

# Case: X-out, Y-in 
def DPAMM_YforX(amountX_out):
  currentRatio = balanceY/balanceX
  new_balanceX = balanceX - amountX_out
  new_balanceY = (balanceX*balanceY) / new_balanceX # K / new_balanceX
  newRatio = new_balanceY/new_balanceX
  new_price = (newRatio/currentRatio) * priceX
  amountY_in = new_balanceY-balanceY
  setBalances(new_balanceX, new_balanceY)
  setPrices(new_price)
  print("~ Swap X out for: ", amountX_out,"token")
  print("new price of X: ", new_price)
  print("new price of Y: ", 1/new_price)
  print()
  return (amountY_in)



# Case X-in, Y-out
def DPAMM_XforY(amountY_out):
  currentRatio = balanceY/balanceX
  new_balanceY = balanceY - amountY_out
  new_balanceX = (balanceX*balanceY)/new_balanceY
  newRatio = new_balanceY/new_balanceX
  new_price = (newRatio/currentRatio) * priceX
  amountX_in = new_balanceX-balanceX
  setBalances(new_balanceX, new_balanceY)
  setPrices(new_price)
  print("~ Swap Y out for: ", amountY_out,"token")
  print("new price of X: ", new_price)
  print("new price of Y: ", 1/new_price)
  print()
  return (amountX_in)


