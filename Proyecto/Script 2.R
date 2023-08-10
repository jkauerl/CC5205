library(ggplot2)
library(dplyr)
library(corrplot)

data <- read.csv("DatosFinales.csv")
head(data)

data$Severity <- case_when(
  data$Severity %in% c("Minor accident") ~ 0,
  data$Severity %in% c("Serious accident") ~ 1)

matriz_cor <- cor(data[, c(2,3,7,8,9,10,11,12,13)])
print(matriz_cor)

corrplot(matriz_cor, method = "color", col = colorRampPalette(c("blue", "white", "red"))(100), tl.col = "black", tl.srt = 45, tl.cex = 0.7)