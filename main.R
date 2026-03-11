source("config.R")
 
source("data/load_data.R")
source("preprocessing/clean_data.R")
source("preprocessing/feature_engineering.R")
 
source("models/train_model.R")
source("models/predict_model.R")
 
source("evaluation/metrics.R")
source("evaluation/visualize.R")
 
source("utils/logger.R")
 
log_message("Starting ML Pipeline")
 
data <- load_dataset()
 
clean <- clean_data(data)
 
features <- create_features(clean)
 
model <- train_model(features)
 
pred <- make_predictions(model, features)
 
score <- calculate_mse(pred, features$y)
 
plot_results(features$y, pred)
 
log_message(paste("Final MSE:", score))
