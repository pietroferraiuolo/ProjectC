#NoEnv  ; Usa solo variabili locali per evitare conflitti
#SingleInstance Force

; Specifica il percorso della cartella e dello script Ruby
scriptDir := "G:\Archive\New Pokemon\ProjectC"
scriptName := "scripts_combine.rb"

; Cambia directory ed esegui lo script Ruby
Run, cmd.exe /K "cd /d %scriptDir% && ruby %scriptName% && exit"