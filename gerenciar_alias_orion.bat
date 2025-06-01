@echo off
setlocal EnableDelayedExpansion

set HOSTS_PATH=%SystemRoot%\System32\drivers\etc\hosts
set ENTRY=127.0.0.1    orion.local
set TMPFILE=%TEMP%\hosts_temp.txt
set SCRIPT_MODE=%1

:: Verifica se está como admin
openfiles >nul 2>&1
if %errorlevel% NEQ 0 (
    echo.
    echo [ERRO] Este script precisa ser executado como ADMINISTRADOR.
    echo Clique com o botao direito e escolha "Executar como administrador".
    pause
    exit /b
)

:: Adicionar alias
if "%SCRIPT_MODE%"=="" (
    echo.
    echo [INFO] Verificando se o alias orion.local já está presente...

    findstr /C:"%ENTRY%" "%HOSTS_PATH%" >nul
    if %errorlevel%==0 (
        echo.
        echo [OK] Alias orion.local já existe no arquivo hosts.
    ) else (
        echo.
        echo [INFO] Adicionando alias ao arquivo hosts...
        echo.>>"%HOSTS_PATH%"
        echo %ENTRY%>>"%HOSTS_PATH%"
        echo.
        echo [SUCESSO] Alias orion.local adicionado com sucesso.
    )
    echo.
    echo Para remover futuramente, execute: gerenciar_alias_orion.bat remover
    pause
    exit /b
)

:: Remover alias
if /I "%SCRIPT_MODE%"=="remover" (
    echo.
    echo [INFO] Removendo alias orion.local...

    (for /f "usebackq tokens=*" %%A in ("%HOSTS_PATH%") do (
        set "line=%%A"
        echo !line! | findstr /C:"%ENTRY%" >nul
        if !errorlevel! NEQ 0 (
            echo !line!>>"%TMPFILE%"
        )
    ))

    copy /Y "%TMPFILE%" "%HOSTS_PATH%" >nul
    del "%TMPFILE%"
    echo.
    echo [SUCESSO] Alias orion.local removido do arquivo hosts.
    pause
    exit /b
)

:: Ajuda
echo.
echo [USO]
echo   gerenciar_alias_orion.bat           ^<-- adiciona o alias
echo   gerenciar_alias_orion.bat remover   ^<-- remove o alias
pause
