# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient


def main():

    #SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
    SUBSCRIPTION_ID="660c1efb-a648-4344-9a03-242ed79e6af5"
    GROUP_NAME = "rg-network-hlg"
    VIRTUAL_NETWORK_NAME = "VNET-HUB-BRSOUTH-HLG"

    # Create client
    # For other authentication approaches, please see: https://pypi.org/project/azure-identity/
    resource_client = ResourceManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )
    network_client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )

    # Get virtual network
    network = network_client.virtual_networks.get(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME
    )
    #print("Get virtual network:\n{}".format(network))

    json_dict = json.dumps(network, default=lambda obj: obj.__dict__, indent=4)
    print(json_dict)
    
    with open ("network.json", "w") as file:
      file.write(json_dict)

    
    
    data = json_dict["address_space"]
    print(data)

if __name__ == "__main__":
    main()
