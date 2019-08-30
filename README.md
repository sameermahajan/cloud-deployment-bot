You can perform your cloud deployments using this bot.

You can say something like

***I would like to deploy EC2 machines of t2.micro having ubuntu using key sameer***

and achieve one utterance deployment! Or you can interact with the bot specifying values for each parameter as you are prompted, until it gathers all values and launches the deployment. Here is a screenshot of a sample interaction with its slack integration:

![Cloud Deployment Bot Sample Interaction](https://github.com/sameermahajan/cloud-deployment-bot/blob/master/images/SlackInteraction.JPG)

For how to create a custom bot in AWS Lex with AWS Lambda, you can take a look at article https://chatbotsmagazine.com/quick-start-develop-a-chat-bot-with-aws-lex-lambda-part-1-b6f7c80ebba6

## lex_bot.json

It is the json for the AWS lex bot.

## lambda_function.py

It is the python code for back end logic in lambda. 
