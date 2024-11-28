
import sys
sys.path.insert(0,'/DEFINE-YOUR-PATH-HERE/Basic-Swap-DPAMM-CPAMM/src') # add your path
import DPAMM

DPAMM.setBalances(12,500000)
DPAMM.setPrices(DPAMM.balanceY/DPAMM.balanceX)

def logDPAMM(): 
    print("------------------------------------")
    print("Price of X: ", DPAMM.priceX)
    print("Balance of X: ",DPAMM.balanceX)
    print("Balane of Y: ", DPAMM.balanceY)
    print("------------------------------------")
    print()

# Swap back and forth, should return both balances and prices to the orginal state(before swap)
# specify number of token-out and which token it is (0 = X, else Y)
def swapDPAMM(amountOut, tokenOut):
    print("***** DPAMM *****")
    logDPAMM()
    if tokenOut == 0:
        result = DPAMM.DPAMM_YforX(amountOut)
        DPAMM.DPAMM_XforY(result)
    else:
        result = DPAMM.DPAMM_XforY(amountOut)
        DPAMM.DPAMM_YforX(amountOut)
    logDPAMM()


swapDPAMM(10, 0)
