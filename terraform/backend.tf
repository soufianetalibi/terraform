terraform {
  backend "azurerm" {
    resource_group_name  = "RG-Storage-Free"
    storage_account_name = "monblobfree2025"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
