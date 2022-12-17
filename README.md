# Phishing-Emails

## Project Aim
The aim of this project is to find Phishing emails using the meta data of emails. Going forward I think that an NLP aproach, or a hybride between this and an NLP 
aproach would preform better

## How it Works
This project works by taking the meta data from emails and classifing the emails bettween phishing or not. The final aproach that I found was the best is uising catboost classifier. There is potential to improve on the time required for training and testing if you were to run this on the GPU, I found that my CPU was good enough for the size of data set used for training. However I would recomend a bigger training set so leveraging the GPU could be worth it. I have also attached my traing data, but as I've previously said I would recemend more data.
