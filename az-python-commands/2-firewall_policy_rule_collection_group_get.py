from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
import json

"""
# PREREQUISITES
    pip install azure-identity
        pip install azure-mgmt-network
# USAGE
    python firewall_policy_rule_collection_group_get.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


client = NetworkManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id="660c1efb-a648-4344-9a03-242ed79e6af5",
)
response = client.firewall_policy_rule_collection_groups.get(
    resource_group_name="rg-network-hlg",
    firewall_policy_name="AFW-POL-01-HLG",
    rule_collection_group_name="DefaultNetworkRuleCollectionGroup",
)

#print(json.load(response))

json_dict = json.dumps(response, default=lambda obj: obj.__dict__, indent=4)
print(json_dict)
      
#data_json = json.load(json_dict)
#print(type(data_json))

#print(data_json["provisioning_state"])

#additional_properties = response.additional_properties    
#print (additional_properties)

#additional_properties = response.provisioning_state
#print (additional_properties) 