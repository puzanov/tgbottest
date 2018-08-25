This is simple tool which can test Telegram bots availability just sending the "/start" message and waiting for any response. 

When bot answers the tool prints OK to STDOUT. If bot does not answer during 4 seconds the tool prints FAIL to STDOUT. 

The tool acts as a regular Telegram user, so we need to do some preparation in order to use it on a fully automatic manner. 

1. Sign up for Telegram using any application.
Log in to your Telegram core: https://my.telegram.org.
Go to ‘API development tools’ and fill out the form.
You will get basic addresses as well as the api_id and api_hash parameters required for user authorization.
For the moment each number can only have one api_id connected to it.

2. After that you will have api_id and api_hash. Put this vars in config.ini file. You should create it in the dir where the tool is
config.ini should be like this
```
[pyrogram]
api_id = 123456
api_hash = "e1503dbbe4906f8526a9ec0a92c85900"
```

3. Now we a ready to install needed libs for the tool. Run sudo pip3 install -r requirements.txt
Note that the tool needs python3, >= 3.4 to be precise. I have tested on python3.6 on Ubuntu and all worked fine. 

4. We are ready to make a first run: ./test.py @my_bot_name
At this point the tool will ask you to enter your Telegram user phone number. Enter it and that enter a confirmation code.
This will happen only once. After a valid confirmation process the tool will create a my_account.session. This file is 
your valid Telegram session. While the file exists and session is valid the tool should skip the validation process on future runs and 
will start to send messages to a bot. 

The second run will be like this:
./test @my_bot_name
OK

5. Here we are. Now you can integrate this tool to a DataDog pipeline and monitor your bots availability.
