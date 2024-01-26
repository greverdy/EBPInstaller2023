[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://ecoris.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://ecoris.com)
[![forthebadge](https://forthebadge.com/images/badges/designed-in-ms-paint.svg)](https://forthebadge.com)


# 🗂️ EBP Installer 2023

L'exécutable "EBP2023.exe" vous permettra d'installer la suite de logiciel EBP en fonction de vos choix.<br>

> **Note**
> Logiciels disponibles :
- EBP Open Line 2023 Autonome Paie | V.13_23_1_14362
- EBP Open Line 2022 Classic BusinessPlan | V.14_0_0_2005
- EBP Open Line 2023 CRM ELITE | V.15_0_0_1305
- EBP 2023 Immobilisations ELITE | V.22_0_0_3735
- EBP 2023 Comptabilite ELITE | V.22_3_1_10778
- EBP 2023 Etats Financiers PRO | V.22_3_0_4116
- EBP 2023 Gestion ELITE | V.22_2_0_7405
***

Code source disponible dans l'archive.<br>
> **Warning** <br> Le code source ne comporte pas les licences.<br>

> **Note** <br> Script compilé à l'aide du module : <a href='https://pypi.org/project/pyinstaller/' target="_blank">pyinstaller</a>.<br>
L'archive est ensuite compilé à l'aide de <a href='https://jrsoftware.org/isinfo.php' target="_blank">Inno Setup</a>.

```bash 
pyinstaller --noconfirm --windowed --icon "<path_to_ico>/EBP2023.ico" --name "EBP2023" --clean --version-file "<path_to_version_file>/file_version_info.txt" --manifest "<path_to_manifest>/manifest.xml" --codesign-identity "ECORIS" --uac-admin --add-data "<path_to_package>/site-packages/customtkinter;customtkinter/"  "<path_to_py>/EBP2023.py"
```

## 💻 How To Use
> **Note**<br>
> Une fois que vous avez téléchargé le fichier d'installation "Ecoris_EBP2023_v1.6.0.exe", suivez les étapes d'installation pour extraire l'utilitaire. Celui-ci sera ensuite accessible sur votre bureau, et vous pouvez le désinstaller à tout moment via le panneau de configuration.

## 🔧 TroubleShooting

- Systèmes d'exploitation supportés : Windows [sans le mode S ⚠] ;
- Désactiver le mode S : <a href="https://support.microsoft.com/fr-fr/windows/sortie-du-mode-s-dans-windows-4f56d9be-99ec-6983-119f-031bfb28a307">Sortie du mode S dans Windows</a> ; 
- Vérifier que vous n'avez aucune mise à jour en attente ⚠ ;
- <a href="mailto:informatique@ecoris.fr?subject=Problème avec l'application : EBPInstaller&body= --- Merci de détailler au mieux votre demande pour que nous puissions vous aider au plus vite ---" target="_blank"> Signaler une erreur / Autres problèmes / Suggestions ➡ à : informatique@ecoris.fr ;</a>
