[Setup]
SetupIconFile=icon.ico
AppCopyright=Thomas Meyer
AppName=Youtube Downloader
AppVerName=Youtube Downloader
UsePreviousAppDir=false
DisableDirPage=yes
DefaultDirName={code:DefDirRoot}\youtube_dl
OutputDir=Output
OutputBaseFilename=Youtube Downloader
ShowLanguageDialog=auto
DisableProgramGroupPage=yes
UsePreviousGroup=false
PrivilegesRequired=admin
AlwaysUsePersonalGroup=true
DefaultGroupName=Thomas Meyer

[Files]
Source: "dist\*"; DestDir: {code:DefDirRoot}\youtube_dl\; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: {commondesktop}\YoutubeDL; Filename: {code:DefDirRoot}\youtube_dl\gui.exe;IconFilename: {code:DefDirRoot}\youtube_dl\icon.ico;
Name: {commonstartmenu}\YoutubeDL; Filename: {code:DefDirRoot}\youtube_dl\gui.exe;IconFilename: {code:DefDirRoot}\youtube_dl\icon.ico;

[Code]
function InitializeSetup(): Boolean;
var
  Path : String;
Begin
  Result:=True;  
  Path      := ExpandConstant('{code:DefDirRoot}\youtube_dl');
  if DirExists(Path) then begin
     DelTree(Path, True, True, True);
  end;
end;

function IsRegularUser(): Boolean;
begin
      Result := not (IsAdminLoggedOn or IsPowerUserLoggedOn);
end;

function DefDirRoot(Param: String): String;
begin
  if IsRegularUser then
     Result := ExpandConstant('{localappdata}')
  else
    if IsWin64 then
      Result := ExpandConstant('{pf32}')
    else 
      Result := ExpandConstant('{pf}')
end;

[Run]

Filename: {code:DefDirRoot}\youtube_dl\gui.exe; WorkingDir: {code:DefDirRoot}\youtube_dl\; Description: "Run Downloader "; Flags: PostInstall; 
