grade = float(input()) #input fyrir einkunir
#ég byrja á að gefa öllum variables tölu. Í þessu tilfelli 0
total_grades = 0 #summan af öllum einkunum sleignar inn
total_credits = 0 # summan af öllum "credits" sem ég nota til að reikna "total_weighted_grade"
total_weighted_grades = 0 # hér er meðal einkun sem verður reiknað með credits á eftir
highest_grade = 0 #hæðsta einkun
while grade >=0: #þegar grade input>= 0 gerist næsta lína og byrjar aftur ef næsta einkun er >=0 osfrv
    credit_score = int(input()) #input fyrir credit score, sem ég mun nota í "weighted average grade"

 #hér segi ég að ef grade er hærra en highest grade sem er 0 fyrst er það highest grade, ef næsta grade er hærra en highest grade er það highest grade. Þannig finn ég highest grade og prenta það síðan í outputið í lokin
    if grade> highest_grade:
        highest_grade = grade

    total_grades +=grade #summan af öllum einkunum + grade sem er input fyrir einkunir
    total_credits += credit_score #summan af öllum credit_score
    total_weighted_grades += grade * credit_score #summan af total_weighted_grades sem ég nota á eftir til að reikna weigted_ average
    grade = float(input()) #aftur beðin um input og fer aftur upp í ln7 ef einkun er > -1
if total_credits != 0: #ef total_credits er ekki 0 halda eftirfarandi reikningar áfram ef þeir eru 0 prentar forritið út tóman streng sem 
    weighted_average = total_weighted_grades / total_credits #hér er "weighted average grade reiknað"
    print (f"Weighted average grade: ", float(round(weighted_average, 2)))#prentum outputið weighted average grade og notum 2 aukastafi
else:
    print()
if highest_grade == 0:
    print ()
else:
    print (f"Highest grade: ", (round(highest_grade, 2))) #prentum outputið highest graded og notum 2 aukastafi
