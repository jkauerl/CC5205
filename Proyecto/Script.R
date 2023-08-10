library(ggplot2)
library(dplyr)
library(corrplot)

data <- read.csv("DatosFinales sin undersampling.csv")
head(data)

data$Severity[data$Severity == 1] <- 0
data$Severity[data$Severity == 2] <- 0
data$Severity[data$Severity == 3] <- 1
data$Severity[data$Severity == 4] <- 1


matriz_cor <- cor(data[, c(2,3,7,8,9,10,11,12,13)])
print(matriz_cor)

corrplot(matriz_cor, method = "color", col = colorRampPalette(c("blue", "white", "red"))(100), tl.col = "black", tl.srt = 45, tl.cex = 0.7)