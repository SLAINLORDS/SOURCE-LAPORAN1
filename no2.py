emas1 = 650000
emas2 = 685000
emas3 = 715000
harga1 = emas1*25
harga2 = emas2*25
harga3 = emas2*15
harga4 = emas3*40
modal1 = harga1
modal2 = harga1 + harga3
keuntungan1 = harga2-harga1
keuntungan2 = harga4-modal2
persen1 = (keuntungan1/modal1)*100
persen2 = (keuntungan2/modal2)*100
#Kasus Pertama:
print ("keuntungan Gerald dalam kasus ini saat emas berharga 685000 adalah = ", keuntungan1)
print ("keuntungan Gerald dalam persen saat emas berharga 685000 adalah = ",round(persen1,2),"%")
#Kasus Kedua:
print ("keuntungan Gerald dalam kasus ini saat emas berharga 715000 adalah = ", keuntungan2)
print ("keuntungan Gerald dalam persen  saat emas berharga 715000 adalah = ",round(persen2,2), "%")