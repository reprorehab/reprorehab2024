library(tidyverse) # data formatting and graphing tools

#Demonstrating histogram for one numeric variable
hist(dataframe$variable)
#Changing number of bins from default to 30
hist(dataframe$variable, breaks=30)

#Demonstrating scatterplot for two numeric variables
plot(dataframe$variable1, dataframe$variable2)
#Changing axes limits to 0 to 10
plot(dataframe$variable1, dataframe$variable2, xlim=c(0,10), 
ylim=c(0,10))

#Demonstrating boxplot using ggplot
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) +  
  geom_boxplot() + 
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") 

#Changing theme from default to minimal
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) +  
  geom_boxplot() + 
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") +
  theme_minimal()  

#Adding raw data with geom_jitter
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) +  
  geom_boxplot() + 
  geom_jitter() +
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") +
  theme_minimal() 

#Removing duplicated outliers by indicating outlier shape
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) +  
  geom_boxplot() + 
  geom_jitter(outlier.shape = NA) +
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") +
  theme_minimal() 

#Decreasing the x jitter, removing the y jitter, and making the datapoints transparent
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) +  
  geom_boxplot() + 
  geom_jitter(width = 0.1, height = 0, alpha = 0.3) +
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") +
  theme_minimal() 

#Demonstrating violin plot using ggplot
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable, color = categoricalvariable)) + 
  geom_violin()

#Modifying violin plot
ggplot(dataframe, aes(x = categoricalvariable, y = numericvariable)) + 
  geom_violin(color = dataframe$categoricalvariable) + 
  geom_jitter(width = 0.2, height = 0, alpha = 0.3) +
  labs(title = "Title",
       x = "X Axis Label", 
       y = "Y Axis Label") +
  theme_minimal() 

