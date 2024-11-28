# Global Variables
balanceX = 0
balanceY = 0

# set the balance of both tokens
def setBalances(balX, balY):
  global balanceX, balanceY
  balanceX = balX
  balanceY = balY

# get the price of token X in Y term
def getPriceX():
  return balanceY/balanceX

# get the price of token Y in X term
def getPriceY():
  return balanceX/balanceY

# Case: X-out, Y-in
def CPAMM_YforX(amountX_out):
  liquidity = balanceX * balanceY
  amountX = balanceX - amountX_out
  amountY_new = liquidity/amountX
  new_price = amountY_new/amountX

  amountY_in  =amountY_new - balanceY
  setBalances(amountX, amountY_new)
  print("~ Swap X out for: ", amountX_out,"token")
  print("new price of X: ", new_price)
  print("new price of Y: ", 1/new_price)
  print()
  return amountY_in



# Case X-in, Y-out
def CPAMM_XforY(amountY_out):
  liquidity = balanceX * balanceY
  amountY= balanceY - amountY_out
  amountX_new = liquidity/amountY
  new_price = amountX_new/amountY
  amountX_in  =amountX_new - balanceX

  setBalances(amountX_new, amountY)
  print("~ Swap Y out for: ", amountY_out,"token")
  print("new price of X: ", 1/new_price)
  print("new price of Y: ", new_price)
  print()
  return amountX_in

