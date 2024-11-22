# Basic-Swap-DPAMM-CPAMM

This repo is a minimal proof of the concept that DPAMM can replicate the characteristic of CPAMM when both supply is set proportionally correspondingly to the price.

## What we did

1. Create a pair of token X and Y
2. Set the supply of `X to 12, and Y to 500000`
3. Set the price of each token based on CPAMM pricing, which is `price of X = Y/X = 41666.666666666664 and price of Y = X/Y = 0.000024`
4. Try swap X for Y.
5. Use entire Y acquired from the previous swap to swap back for X.
   > Note: There is no trading fees charged here, so `k` remains stable
6. Do everything aboev to DPAMM
7. Compare if both CPAMM and DPAMM provide the same result.
   > Note: that there could be overflow/underflow occur, especially in DPAMM which requires extra computation. The compromise we accept for the error threshold is `0.1%`.

## Result Summary

Both CPAMM and DPAMM yield the exact same result. This proves that DPAMM can replicate CPAMM's curve behaviour if the setting matches.

Result from CPAMM
`------------------------------------
Price of X: 41666.666666666664
Balance of X: 12
Balane of Y: 500000

---

~ Swap X out for: 10 token
new price of X: 1500000.0
new price of Y: 6.666666666666667e-07

~ Swap Y out for: 2500000.0 token
new price of X: 41666.666666666664
new price of Y: 2.4e-05

---

Price of X: 41666.666666666664
Balance of X: 12.0
Balane of Y: 500000.0
------------------------------------`

Result from DPAMM
`------------------------------------
Price of X: 41666.666666666664
Balance of X: 12
Balane of Y: 500000

---

~ Swap X out for: 10 token
new price of X: 1500000.0
new price of Y: 6.666666666666667e-07

~ Swap Y out for: 2500000.0 token
new price of X: 41666.666666666664
new price of Y: 2.4e-05

---

Price of X: 41666.666666666664
Balance of X: 12.0
Balane of Y: 500000.0
------------------------------------`

## Guide

Clone this repository
`git clone https://github.com/Ax11-Labs/Basic-Swap-DPAMM-CPAMM.git`

Go to the downloaded repo, make sure you have [Python3](https://www.python.org/downloads/) on your computer, and run:
`python3 ./test/Test.py

Adjust the value within the `SwapTest.py` as you like for more experiments.

## Contribution

This repository is made open-source with the MIT license. In short, just do whatever you want.
