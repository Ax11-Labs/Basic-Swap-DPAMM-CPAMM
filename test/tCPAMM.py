
import sys
sys.path.insert(0,'/Users/santachatsuwanlertlum/Documents/GitHub/Basic-Swap-DPAMM-CPAMM/src')
import CPAMM

CPAMM.setBalances(12,500000)

def logCPAMM(): 
    print("------------------------------------")
    print("Price of X: ", CPAMM.balanceY/CPAMM.balanceX)
    print("Balance of X: ",CPAMM.balanceX)
    print("Balane of Y: ", CPAMM.balanceY)
    print("------------------------------------")
    print()

# Swap back and forth, should return both balances and prices to the orginal state(before swap)
# specify number of token-out and which token it is (0 = X, else Y)
def swapCPAMM(amountOut, tokenOut):
    print("***** CPAMM *****")
    logCPAMM()
    if tokenOut == 0:
        result = CPAMM.CPAMM_YforX(amountOut)
        CPAMM.CPAMM_XforY(result)
    else:
        result = CPAMM.CPAMM_XforY(amountOut)
        CPAMM.CPAMM_YforX(amountOut)
    logCPAMM()


swapCPAMM(10, 0)
