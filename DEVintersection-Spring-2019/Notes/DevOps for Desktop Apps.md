# DevOps for Desktop Apps

https://aka.ms/devops4clientapps

> MSIX is the package format to deploy ANY Windows application

- MFC
- Win32
- UWP
- .NET FW
- .NET Core 3
- Etc

Publishing Anywhere

- Managed: Store, Intone, CSSM
- Unmanaged: (Web, UNC)

## Visual Studio Application Packaging Project (.wapproj)

- Create MSIX with Visual Studio
- Manifest Editor
- Debugging
- Packages Wizard
- MSBuild based (Customize build/package with MSB properties)

## Configuring automatic updates with the `.appistaller`

> XML Document

## Yeah so this only works on Windows 10

For new apps, go with a web app, deploy with chromium if you have to. The designer for managing MSIX installer packages looks really cool though.

Also, you can store secure files in Azure DevOps for signing your application as a step in a release pipeline, so that's pretty cool.




















































