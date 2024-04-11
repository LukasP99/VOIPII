from asterisk.ami import AMIClient, SimpleAction
from voip2_backend.settings import C

class AmiContextManager:
    def __enter__(self):
        self.client = AMIClient(address=C.ASTERISK_IP, port=C.ASTERISK_PORT)
        self.client.login(username=C.AMI_USERNAME, secret=C.AMI_PASSWORD)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.logoff()


def make_call(from_ext, to_ext):
    with AmiContextManager() as client:
        action = SimpleAction(
            "Originate",
            Channel=f"Local/{from_ext}@from-ami",
            Exten=f"{to_ext}",
            Priority=1,
            Context="from-internal",
            CallerID=f"{to_ext}",
        )
        client.send_action(action)
