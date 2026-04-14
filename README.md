# terraform
workflow .yml permet d'executer deux étapes CI et CD : 

1- on push : l'execute un script python qui test la connexion à azure

2- si l'étape 1 est OK, j'execute le code terraform qui permet de déployer ce qui est défini dans main.tf et mettre à jour le fichier tfstate présent sur un storage account azure.

======

je peux déclencher le code (Azure CLI, Bicep, Terraform) via un script PowerShell sur ma machine ou via un workflow .yml sur github

Ici, le workflow .yml sur github contient des commandes terraform, il se connecte sur azure avec un SP et exécute des commandes terraform pour créer des ressources sur 
azure

======


echo "# terraform" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/soufianetalibi/terraform.git

git push -u origin main



push an existing repository from the command line

git remote add origin https://github.com/soufianetalibi/terraform.git

git branch -M main

git push -u origin main


======
Exemple : 
======

un code terraform PRO qui permet de créer une pipeline CI/CD via l'IaC Terraform
ce code se déclenche par un simple


repo/
 ├ terraform/
 │   ├ main.tf
 │   ├ variables.tf
 │   ├ outputs.tf
 │   ├ provider.tf
 │   ├ backend.tf
 │   ├ terraform.tfvars
 │
 └ .github/
     workflows/
       deploy.yml


✔ CI fonctionne   (test, build)
✔ CD fonctionne   (deploy)
✔ Azure connecté
✔ Infra créée
✔ Pipeline automatique
✔ Repo prêt pour projet pro

===========================================
je peux lancer terraform depuis : 
-Repo github via un workflow
-depuis une machine local linux ou windows
-depuis un conteneur

cmd : 

terraform init : initialisation 
terraform plan : prévisualiser les changements
terraform apply : appliquer les changements

--> le workflow permet de lancer toutes ces étapes.
