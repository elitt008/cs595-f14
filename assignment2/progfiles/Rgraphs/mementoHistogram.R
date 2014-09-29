png(filename="mementoCount.png",height=512,width=512,bg="white")
memento_data <- read.table("hist1.dat")
memento_counts <- table(memento_data)
max_num <- max(memento_counts)
histinfo <- hist(memento_counts, xlab="Number of Mementos",ylab="Number of Occurances",col="lightblue", breaks=150, xlim=c(0,max_num),right=F, main="Memento Histogram", las=1)
dev.off()

png(filename="mementoCountmax.png",height=512,width=512,bg="white")
histinfo <- hist(memento_counts, xlab="Number of Mementos",ylab="Number of Occurances",col="lightblue", breaks=max_num, xlim=c(0,max_num),right=F, main="Memento Histogram", las=1)
dev.off()

