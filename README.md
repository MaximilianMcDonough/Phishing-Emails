# Phishing-Emails

## Project Aim
Using the meta data of email messages, this project aims to detect phishing emails. Going forward, I think that an NLP approach, or a hybrid approach of this and an NLP approach would be more effective.

## How it Works
I classified emails based on their meta data to determine if they were phishing or not in this project. As a final approach, I used Catboost to classify emails. Using the GPU would reduce the time it takes to train and test; my CPU was sufficient for the amount of data I used; if you used the GPU, the time would be reduced. If, however, you choose to expand on the training data I have attached, it may be worthwhile to leverage the GPU. In addition, I have attached my training data, but as I have previously stated, I recommend that more data be collected.
