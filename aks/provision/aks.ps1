# Login no Azure
Connect-AzAccount

#Criar Grupo de Recursos
New-AZResourceGroup -Name "rg-aks-pwsh" -Location "East US"

#Criar AKS
New-AzAksCluster -ResourceGroup "rg-aks-pwsh" -Name "aks-powershell" -NodeCount 1

#Listar clusters do AKS
Get-AzAksCluster

#INstalar kubect
Install-AzAksKubectl

#Importar as credencias
Import-AzAksCredential -ResourceGroup "rg-aks-pwsh" -Name "aks-powershell"

#Listar node com o kubectl
kuberctl get nodes

#Excluir aks
Remove-AzAksCluster -ResourceGroup "rg-aks-pwsh" -Name "aks-powershell"

