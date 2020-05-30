queries <- c('q1','q1','q2','q2','q3','q3','q4','q4','q5','q5','q6','q6','q7','q7')
testType <- c('FO','GT','FO','GT','FO','GT','FO','GT','FO','GT','FO','GT','FO','GT')
queries <- c('q1','q1','q2','q2','q3','q3','q4','q4','q5','q5','q6','q6','q7','q7')
value <- c(0.093,0.253,67.961,0.259,14.118,0.25,13.989,0.24,0.09,0.272,0.097,0.264,0.089,0.27)
ggplot(data, aes(fill=testType,y=value,x=queries)) + geom_bar(position="dodge", stat="identity")+
  ggtitle("Execution time for different queries")+ xlab("")+ ylab("Time in seconds")