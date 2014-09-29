png(filename="timevmementolog.png",height=512,width=512,bg="white")
creation_data <- read.table("../creation_vs_mementos.dat")
plot(creation_data$V1,creation_data$V2,type="p",xlab="Estimated Creation Time (hours)",ylab="Number of Mementos",log="xy")
dev.off()

png(filename="timevmemento.png",height=512,width=512,bg="white")
plot(creation_data$V1,creation_data$V2,type="p",xlab="Estimated Creation Time (hours)",ylab="Number of Mementos")
dev.off()

