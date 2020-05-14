require("ggplot2")

#y1<-c(28.826 , 59.964,59.964+28.826,59.964+2*28.826,59.964+3*28.826)
#y2<-c(14.368, 30.115, 45.209, 59.715, 78.820)

x<-1:5
ggplot(data.frame(x,y1,y2),aes(x))+
  ggtitle("cpu : 20% inc / yes instance / q1 (red fo, green g&t)")+
  xlab("entries (Million)")+
  ylab("time (sec)")+
  geom_line(aes(y=y1), colour="green")+
  geom_line(aes(y=y2), colour="red")+
  geom_point(aes(y=y1), colour="green")+
  geom_point(aes(y=y2), colour="red")


#y1<-c(26.327, 55.969, 87.699,87.699+(55.969-26.327),87.699+2*(55.969-26.327))
#y2<-c(11.680, 24.444, 37.046, 49.055, 61.611)

x<-1:5
ggplot(data.frame(x,y1,y2),aes(x))+
  ggtitle("cpu : 20% inc / no instance / q1 (red fo, green g&t)")+
  xlab("entries (Million)")+
  ylab("time (sec)")+
  geom_line(aes(y=y1), colour="green")+
  geom_line(aes(y=y2), colour="red")+
  geom_point(aes(y=y1), colour="green")+
  geom_point(aes(y=y2), colour="red")

#y1<-c(10000000, 20000000,30000000,40000000,50000000)
#y2<-c(2600002, 5200002, 7800002, 10400002, 13000002)

x<-1:5
ggplot(data.frame(x,y1,y2),aes(x))+
  ggtitle("rules : 20% inc / yes instance / q1 (red fo, green g&t)")+
  xlab("entries (Million)")+
  ylab("rules")+
  geom_line(aes(y=y1), colour="green")+
  geom_line(aes(y=y2), colour="red")+
  geom_point(aes(y=y1), colour="green")+
  geom_point(aes(y=y2), colour="red")

#y1<-c(7737025, 15468905, 23203990,23203990+(15468905-7737025),23203990+2*(15468905-7737025))
#y2<-c(2394333, 4788289, 7181959, 9576169, 11970271)

x<-1:5
ggplot(data.frame(x,y1,y2),aes(x))+
  ggtitle("rules : 20% inc / no instance / q1 (red fo, green g&t)")+
  xlab("entries (Million)")+
  ylab("rules")+
  geom_line(aes(y=y1), colour="green")+
  geom_line(aes(y=y2), colour="red")+
  geom_point(aes(y=y1), colour="green")+
  geom_point(aes(y=y2), colour="red")
