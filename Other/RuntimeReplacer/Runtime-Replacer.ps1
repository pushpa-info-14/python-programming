function Update-RuntimeBlock {
    param (
        [Parameter(Mandatory=$true)]
        [string]$NewConfig,

        [Parameter(Mandatory=$true)]
        [string]$TargetConfig
    )

    # Validate files
    if (-not (Test-Path $NewConfig)) {
        throw "New config file not found: $NewConfig"
    }

    if (-not (Test-Path $TargetConfig)) {
        throw "Target config file not found: $TargetConfig"
    }

    # Backup target config with timestamp
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupFile = "$TargetConfig.$timestamp.bak"
    Copy-Item -Path $TargetConfig -Destination $backupFile -Force
    Write-Host "Backup created: $backupFile"

    # Read file content as single string
    $newContent    = Get-Content -Path $NewConfig -Raw
    $targetContent = Get-Content -Path $TargetConfig -Raw

    # Find runtime block in new config
    $startTag = "<runtime"
    $endTag   = "</runtime>"

    $startIndex = $newContent.IndexOf($startTag)
    $endIndex   = $newContent.IndexOf($endTag, $startIndex)

    if ($startIndex -eq -1 -or $endIndex -eq -1) {
        throw "No <runtime> block found in $NewConfig"
    }

    $endIndex += $endTag.Length
    $runtimeBlock = $newContent.Substring($startIndex, $endIndex - $startIndex)

    # Replace runtime block in target config
    $tStartIndex = $targetContent.IndexOf($startTag)
    $tEndIndex   = $targetContent.IndexOf($endTag, $tStartIndex)

    if ($tStartIndex -ne -1 -and $tEndIndex -ne -1) {
        $tEndIndex += $endTag.Length
        $updatedContent = $targetContent.Substring(0, $tStartIndex) + $runtimeBlock + $targetContent.Substring($tEndIndex)
        Write-Host "Runtime block replaced in target config."
    } elseif ($targetContent.Contains("</configuration>")) {
        # Insert before </configuration> if not present
        $insertIndex = $targetContent.IndexOf("</configuration>")
        $updatedContent = $targetContent.Substring(0, $insertIndex) + $runtimeBlock + "`r`n" + $targetContent.Substring($insertIndex)
        Write-Host "Runtime block inserted into target config."
    } else {
        throw "Target config does not contain </configuration> tag."
    }

    # Write updated content back
    Set-Content -Path $TargetConfig -Value $updatedContent -Encoding UTF8
    Write-Host "Target config updated successfully."
}

# Example usage
Update-RuntimeBlock `
    -NewConfig "Host.exe-new.config" `
    -TargetConfig "Host.exe.config"
