source("data/generate_data.R")
source("utils/logger.R")
 
load_dataset <- function() {
  log_message("Loading dataset")
  data <- generate_dataset()
  return(data)
}
