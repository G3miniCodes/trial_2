calculate_mse <- function(pred, actual) {
 
  mse <- mean((pred - actual)^2)
 
  return(mse)
}
