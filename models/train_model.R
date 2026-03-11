source("utils/helpers.R")
 
create_features <- function(data) {
 
  data$x1_sq <- square(data$x1)
  data$x2_sq <- square(data$x2)
 
  return(data)
}
