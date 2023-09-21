#input fyrir hvar range-ið okkar á að stoppa
stop_range = int(input())
#input sem við notum til að finna þær tölur sem eru með x marga deilur td 48 er hægt að deila með 10 mismunandi tölum
num_divisors = int(input())


# range 20 minsta og 100 mesta
for i in range(20,min(stop_range, 100)):
#deilir með námundun og næsti deilir og gefur út afgang
    tens = i // 10
    units = i % 10
#hér er summan af 
    square_sum = (tens + units) * (tens + units)
    if square_sum == i:
        print(int(i))
#hér er range-ið notað aftur nema við byrjum í 1
for num in range (1, min (stop_range, 100)):
    #stillum count að 0 til að byrja talinguna á 0 og fer svo up þegar for loopan er reynd aftur
    count = 0
    # hér fer forritið í gegnum tölur hækkandi frá 0
    for divisor in range (1, num + 1):
        #ef tala í range-inu hefur afgangin 0 er hún talin í count fyrir neðan
        if num % divisor == 0:
            
            count += 1
#ef tala frá 1 - num er jöfn num divisor sem er tala með 0 í afgang prentast sú tala/tölur
    if count == num_divisors:
        print(num)
    
