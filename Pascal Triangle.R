x <- 1
print(x)
for (i in 1:5) { x <- c(0, x) + c(x, 0); print(x) }
for (i in 1:5) {y<-2^i;print(y)}

