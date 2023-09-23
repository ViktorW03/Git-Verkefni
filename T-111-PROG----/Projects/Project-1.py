symbol = input("The stock symbol:\n") # input func fyrir td AAPL.bætti við \n
nshares = int(input("Number of shares:\n")) # fjöldi "shares" #bætti við \n
#bætti við \n fyrir neðan
bprice = float(input("The stock buying price:\n")) # kaupverð hlutabréfs
#bætti við \n fyrir neðan
sprice = float(input("The stock selling price:\n")) # söluverð hlutabréfs

total_buying_price = nshares * bprice # heildar verð
buy_comission = total_buying_price * 0.03 # kaup þóknun
n_shares_at_sprice = nshares * sprice # fjöldi "shares" á verðinu x
sell_comision = n_shares_at_sprice * 0.03 # söluþóknun
total_sell_price = n_shares_at_sprice # heildar söluverð
profit_loss = total_sell_price - total_buying_price - buy_comission - sell_comision # hagnaður/tap

#næst prenta ég niðurstöðurnar út frá útreiknungum mínum með streng svo það sé læsilegt fyrir notandan og námunda öll float að 2 aukastöfum

#bætti við ":" fyrir aftan print ("\nTransactions for stock\ og aðrar línur því ég fékk alltaf rangt svar þegar ég skilaði.Fékk líka villu fyrir að vanta \n í input func og hér fyrir neðan svo ég bætti því við
print ("\nTransactions for stock:",symbol) #bætti við ":" og \n
print (f"Bought {nshares} shares @ {round(bprice, 2)}")
print ("Paid", round(total_buying_price,2)) 
print ("Commission when buying:", round(buy_comission,2),) #bætti við ":"
print (f"Sold {nshares} shares @ {round(sprice,2)}")
print ("Received", round(total_sell_price,2))
print ("Commission when selling:", round(sell_comision,2)) #bætti við ":"
print ("Profit or loss:",round(profit_loss,2)) #bætti við ":"










