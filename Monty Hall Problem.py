import random
Door1 = "Goat"
Door2 = "Prize"
Door3 = "Goat"

N = 1000

sample_points = []; Box_Prz=[]; Box_Cho=[];Box_Rev=[]
a=[1,2,3]
for i in range(N):
    Box_Prize = random.choice([1,2,3])
    Box_Chosen = random.choice([1,2,3])
    
    Box_Prz.append(Box_Prize)
    Box_Cho.append(Box_Chosen)
    
    if Box_Prize != Box_Chosen:
        Box_Reveal = sum(a)-Box_Prize-Box_Chosen
    else:
        Box_Reveal = random.choice([s for s in a if s!= Box_Prize])
            
    sample_points.extend([Box_Prize,Box_Chosen,Box_Reveal])
    Box_Rev.append(Box_Reveal)


i = 0
Loss = 0; Win = 0
while i< len(sample_points):
    if sample_points[i] == sample_points[i+1]:
        Loss += 1
    else:
        Win += 1
    i = i+3

   
print("Probability of win with switch ",round(Win/N,2))
print("Probability of win with stay strategy",round(1-(Win/N),2))
#print("Probability of loss with switch",round(Prob_Switch_same * Loss,2))
#print("Probability of loss with stay strategy",round(1-(Prob_Switch_same * Loss),2))

# Box_Prz.count(3)

#[x for x in a if Box_Prize in a and Box_Chosen in a]

## for reference

#for i in range(10):
 #   Box_Prize = random.choice([1,2,3])
  #  Box_Chosen = random.choice([1,2,3])
#
 #   if Box_Prize != Box_Chosen:
  #      Box_Reveal = sum(a)-Box_Prize-Box_Chosen
   # else:
    #    Box_Reveal = [s for s in a if s!= Box_Prize]
            
    #sample_points.extend([Box_Prize,Box_Chosen,Box_Reveal])
