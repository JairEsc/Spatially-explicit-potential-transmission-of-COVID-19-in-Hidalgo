#descripcion de los datos
infectadosAcumulados<-c(2,3,3,3,8,10,10)
infectadosAC5dias=log(infectadosAcumulados[1:5])-log(2)
infectadosAC6dias=log(infectadosAcumulados[1:6])-log(2)
infectadosAC7dias=log(infectadosAcumulados[1:7])-log(2)

#consideraciones
summary(lm(infectadosAC5dias~0+seq(0,length(infectadosAC5dias)-1,1)))
summary(lm(infectadosAC5dias~seq(0,length(infectadosAC5dias)-1,1)))
summary(lm(infectadosAC6dias~0+seq(0,length(infectadosAC6dias)-1,1)))
summary(lm(infectadosAC6dias~seq(0,length(infectadosAC6dias)-1,1)))
summary(lm(infectadosAC7dias~0+seq(0,length(infectadosAC7dias)-1,1)))
summary(lm(infectadosAC7dias~seq(0,length(infectadosAC7dias)-1,1)))

r=coef(summary(lm(infectadosAC7dias~0+seq(0,length(infectadosAC7dias)-1,1))))[[1]]
beta=r+0.344
  