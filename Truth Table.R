P<-function(I)
{
  if(I==1)
  {
    return(matrix(c(T,T)))
  }
  else if(I==2)
  {
    return(matrix(c(T,F)))
  }
  else if(I==3)
  {return((matrix(c(F,T))))
  }
  else{return(matrix(c(F,F)))}
}
P(1)

P<-c(T,T,F,F)
Q<-c(T,F,T,F)

P_and_Q<-(P & Q )
P_or_Q<-P|Q
Not_P<-!P
Not_Q<-!Q
P_implies_Q<-Not_P|Q
Q_implies_P<-Not_Q|P
P_equiv_Q<-P_implies_Q & Q_implies_P
Truth_Table<-data.frame(P,Q,Not_P,Not_Q,P_and_Q,P_or_Q,P_implies_Q,P_equiv_Q)  
print(Truth_Table)  

