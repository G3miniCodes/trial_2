source("config.R")
 
train_model <- function(data) {
 
  if (MODEL_TYPE == "linear_regression") {
 
    model <- lm(y ~ ., data=data)
 
  }
 
  return(model)
}
