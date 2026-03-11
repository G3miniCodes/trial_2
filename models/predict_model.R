make_predictions <- function(model, data) {
 
  predictions <- predict(model, data)
 
  return(predictions)
}
