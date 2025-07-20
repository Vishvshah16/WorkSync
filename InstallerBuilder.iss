#define MyAppName "WorkSync"
#define MyFolderName "WorkSync"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "Vishva Shah"
#define MyAppURL ""
#define MyAppDescription "WorkSync Task Update Tracker"
#define MyAppExeName "WorkSync.exe"
#define DisplayName "WorkSync"
#define RootFolderName "WorkSync"

[Setup]
VersionInfoVersion={#MyAppVersion}
AppId={{xFP2O1xrgkKS6TiJ5os5DA==}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#RootFolderName}\{#MyFolderName}
DisableProgramGroupPage=yes
UsedUserAreasWarning=no
PrivilegesRequired=admin
OutputDir=.\Package\Windows
OutputBaseFilename=WorkSync-{#MyAppVersion}
SetupIconFile=assets\icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern
SetupMutex=SetupMutex{#SetupSetting("AppId")}
UninstallDisplayName={#DisplayName}
UninstallDisplayIcon={app}\{#MyAppExeName}

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall {#MyAppName}"; Filename: "{uninstallexe}"; IconFilename: "{app}\{#MyAppExeName}"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Dirs]
Name:"{app}";Permissions: System-full

[Files]
Source: "dist\WorkSync\WorkSync.exe"; DestDir: "{app}"; Flags: onlyifdoesntexist ; Permissions: system-full
Source: "dist\WorkSync\assets\*"; DestDir: "{app}\assets\"; Flags: ignoreversion recursesubdirs; Permissions: system-full
Source: "dist\WorkSync\_internal\*"; DestDir: "{app}\_internal\"; Flags: ignoreversion recursesubdirs; Permissions: system-full

[Run]
Filename: "{app}\WorkSync.exe"; Flags: nowait runhidden;

[UninstallRun]
Filename: "taskkill"; Parameters: "/F /IM WorkSync.exe"; Flags: runhidden;

[UninstallDelete]
Type: filesandordirs; Name: "{app}\*"
Type: filesandordirs; Name: "{commonappdata}\{#RootFolderName}"
