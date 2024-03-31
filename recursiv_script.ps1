function Explore-Href {
    param (
        [string]$BaseUrl,
        [string]$Path = "/",
        [string]$OutputFile
    )

    $Uri = $BaseUrl + $Path
    $response = Invoke-WebRequest -Uri $Uri

    foreach ($link in $response.Links.href) {
        if ($link -eq "README") {
            $readmeUri = $Uri + $link
            $readmeContent = Invoke-WebRequest -Uri $readmeUri
            $text = [System.Text.Encoding]::UTF8.GetString($readmeContent.Content)
            # Ajouter l'URL au fichier de sortie avant le contenu du README
            "URL: $readmeUri`r`n" | Out-File -FilePath $OutputFile -Append
            # Écrire le contenu dans le fichier de sortie spécifié, en ajoutant
            $text | Out-File -FilePath $OutputFile -Append
            # Ajouter une séparation pour une meilleure lisibilité entre les contenus de README
            "`r`n" | Out-File -FilePath $OutputFile -Append
        }
        elseif ($link -notmatch "\.\.") { # Ignorer les liens vers le répertoire parent
            Explore-Href -BaseUrl $BaseUrl -Path ($Path + $link) -OutputFile $OutputFile
        }
    }
}

# Définit le chemin du fichier de sortie
$OutputFile = "C:\Users\nowi\Desktop\Darkly\ret_readme.txt"

# Base URL de votre recherche
$BaseUrl = "http://192.168.56.101/.hidden/"

# Supprime le fichier de sortie s'il existe déjà pour commencer avec un fichier vierge
if (Test-Path $OutputFile) {
    Remove-Item $OutputFile
}

# Commencez l'exploration et l'enregistrement des README
Explore-Href -BaseUrl $BaseUrl -OutputFile $OutputFile