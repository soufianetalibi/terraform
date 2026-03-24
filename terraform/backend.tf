terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "sttfstate12345"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
