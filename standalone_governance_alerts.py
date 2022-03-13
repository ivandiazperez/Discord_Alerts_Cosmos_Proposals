from discord_webhook import DiscordWebhook
from datetime import datetime
from time import sleep
import pytz
from terra_sdk.client.lcd import LCDClient
from terra_sdk.core.gov import ProposalStatus

class GetNewTerraProposals:
    """A simple class to regularly check for new proposals (in the voting period) for Terra.
    It runs every hour -- update the delay as you like -- and issues a Discord message with the proposal number and the link to Agora"""
    def __init__(self):
        super().__init__()
        self.discord_url = ['https://YOUR_DISCORD_WEBHOOK_ADDRESS_HERE'] #Warning : the brackets must remain.
        self.now = datetime.now(tz=pytz.UTC)  # get the current timestamp, to alert only on new proposals.

    def run(self):

            terra = LCDClient(chain_id="columbus-5", url="https://lcd.terra.dev")

            try:
                proposals = terra.gov.proposals({"proposal_status": ProposalStatus(2)})

                for i in proposals[0]:
                    link = i.content.description.split('\n')[0] #the link to the proposal
                    number = i.proposal_id
                    if i.submit_time > self.now: #the proposal entered the voting period after the previous check, so we should alert.
                        message = f"Proposal {number} is in voting stage!\n{link}"
                        DiscordWebhook(url=self.discord_url, content=message).execute()

                    #now let's update the timestamp so that only later proposals are caught.
                    self.now = datetime.now(tz=pytz.UTC)


            except Exception as e: #catch any possible exception, be it with the lcd query or the discord message.
            #it's all very simple so this is just for the initial debugging, not much point setting up a log or anything more sophisticated.
                print(e)

            sleep(3600) #check for new proposals every hour. Adjust to whatever is more appropriate.

if __name__ == '__main__':
    #Note: this isn't a thread, because as of Python3.9 the LCD query will trigger an exception ("can't register atexit after shutdown")
    #I didn't find a solution to this. It worked with Python3.8 and is possibly resolved with Pyhon3.10, haven't tested.
    GetNewTerraProposals().run()