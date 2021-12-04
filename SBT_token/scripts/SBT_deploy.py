from brownie import network, accounts, config, SBTshady
from brownie.network import account

inital_supply = 100000000000000000000000  # 100,000
token_name = "SBTshady"
token_symbol = "SBT"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    # constructor takes intialSupply in the constructor,
    # hence passing that value when deploying.
    # NOTE: If you take the template from the ethereum website directly then you need to pass
    # tokenName and tokenSymbol also while deploying.
    sbt = SBTshady.deploy(inital_supply, {"from": account}, publish_source=True)
