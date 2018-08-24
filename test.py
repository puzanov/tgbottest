#!/usr/bin/python3.6

from tgintegration import BotIntegrationClient

c = BotIntegrationClient(
        session_name='my_account',
        bot_under_test='@namba_taxi_bot',  # We're going to test the @BotListBot
        max_wait_response=4,  # Wait a max of 10 seconds for responses, ...
        raise_no_response=False,  # ... then check for response.empty instead of raising
        min_wait_consecutive=2.0,  # Wait at least 2 seconds to collect more than one message
        global_action_delay=1.8,  # Space out all messages by 1.8 seconds
    )

c.start(False)

res = c.send_command_await("/start", num_expected=1)
if res.num_messages == 1:
    print("OK")
else:
    print("FAIL")
c.stop()
