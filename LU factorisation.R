i<-round(runif(9,1,100),digits=0)
n<-3
elasticity<-matrix(i,byrow = TRUE,nrow=n,ncol = n)
cd=elasticity 
elasticity
O=matrix(nrow = n,ncol = n)
upper.triangle=matrix(nrow = n,ncol = n)
upper.triangle=elasticity
q=1
while(q<n){
  for(u in (q+1):n){
    O[u,q]=elasticity[u,q]/elasticity[q,q]#calculating multiplier
    for(p in 1:n){
      upper.triangle[u,p]=upper.triangle[u,p]-(O[u,q]*elasticity[q,p])
    }
  }
  elasticity=upper.triangle
  q=q+1
}

round(upper.triangle,digits = 0)

#I eleimination matrix
lower.triangle=matrix(nrow = n,ncol = n)
for(z in 1:n)
  {
  for(x in 1:n)
    {
    if (z==x)
      {
      lower.triangle[z,x]=1
    } 
    if (z<x)
      {
      lower.triangle[z,x]=0
    }
  }
}
lower.triangle
k=1
multiplier=matrix(nrow = n,ncol = n)
elim1=cd 
elim2=matrix(nrow = n,ncol = n) 
while(k<n){
for(z1 in 2:n){
  multiplier[z1,k]=elim1[z1,k]/elim1[k,k]
  lower.triangle[z1,k]=multiplier[z1,k]

  for(z2 in 1:n){
  elim2[z1,z2]=elim1[z1,z2]-(multiplier[z1,k]*elim1[k,z2])
}
  }
  k=k+1
elim1=elim2
}
round(lower.triangle,digits = 0)


lower.triangle%*%upper.triangle
