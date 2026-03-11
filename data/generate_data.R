source("config.R")
 
generate_dataset <- function() {
 
  set.seed(SEED)
 
  x1 <- rnorm(DATA_SIZE)
  x2 <- rnorm(DATA_SIZE)
 
  y <- 3*x1 + 2*x2 + rnorm(DATA_SIZE)
 
  df <- data.frame(x1, x2, y)
 
  return(df)
}
