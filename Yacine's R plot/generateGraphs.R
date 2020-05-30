require("ggplot2")

q1y1<-c(0.082,0.139,0.192,0.28,0.339)
q1y2<-c(0.202,0.414,0.587,0.928,0.913)

q5y1<-c(0.079,0.146,0.184,0.25,0.273)
q5y2<-c(0.221,0.446,0.649,0.926,1.0)

q6y1<-c(0.066,0.121,0.182,0.252,0.284)
q6y2<-c(0.204,0.414,0.603,0.885,0.935)

q7y1<-c(0.059,0.115,0.166,0.256,0.255)
q7y2<-c(0.202,0.438,0.593,0.861,0.921)

x<-1:5
ggplot(data.frame(x,y1,y2),aes(x))+
  ggtitle("cpu : con / q1:green, q5:red, q6:blue, q7:purple")+
  xlab("entries")+
  ylab("time (sec)")+
  geom_line(aes(y=q1y1), linetype = "dashed", colour="green")+
  geom_line(aes(y=q1y2), colour="green")+
  geom_point(aes(y=q1y1), colour="green")+
  geom_point(aes(y=q1y2), colour="green")+
  # Q5
  geom_line(aes(y=q5y1), linetype = "dashed", colour="red")+
  geom_line(aes(y=q5y2), colour="red")+
  geom_point(aes(y=q5y1), colour="red")+
  geom_point(aes(y=q5y2), colour="red")+
  # Q6
  geom_line(aes(y=q6y1), linetype = "dashed", colour="blue")+
  geom_line(aes(y=q6y2), colour="blue")+
  geom_point(aes(y=q6y1), colour="blue")+
  geom_point(aes(y=q6y2), colour="blue")+
  # Q7
  geom_line(aes(y=q7y1), linetype = "dashed", colour="purple")+
  geom_line(aes(y=q7y2), colour="purple")+
  geom_point(aes(y=q7y1), colour="purple")+
  geom_point(aes(y=q7y2), colour="purple")
