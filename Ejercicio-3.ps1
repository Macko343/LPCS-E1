# Scirp para activar o desactivar una lista de servicios en windows
# a partir de un archivo lista

Get-Content -Path $PSScriptRoot\lista.txt -ErrorAction "Stop"


$servicios = Get-Content -Path $PSScriptRoot\lista.txt

function Iniciar-Serv {
    foreach( $servicio in $servicios){
        if (-NOT((Get-service -name $servicio).Status -eq "Running" )){
        Start-Service -name $servicio
        Write-Host "Servicio iniciado: " , $servicio
        }
    }
}

function Detener-Serv {
    foreach( $servicio in $servicios){
        if (-NOT((Get-service -name $servicio).Status -eq "Stopped" )){
        Stop-Service -name $servicio
        Write-Host "Servicio detenido: " , $servicio
        }
    }
}


function Suspender-Serv {
    foreach( $servicio in $servicios){
        try{
            Suspend-Service -name $servicio -ErrorAction "Stop"
            Write-Host "Servicio suspendido: " , $servicio
        } catch{
            Write-Host "Este servicio no se puede suspender: ", $Servicio
        }
    }
}

function Reiniciar-Serv {
    foreach( $servicio in $servicios){
        if (-NOT((Get-service -name $servicio).Status -eq "Stopped" )){
        Restart-Service -name $servicio
        Write-Host "Servicio reiniciado: " , $servicio
        }
    }
}

$accion = 0
while(-not($accion -ceq 5) ){
    Write-Host "Opciones en este script:"
    Write-Host "   1.- Iniciar servicios"
    Write-Host "   2.- Detener servicios"
    Write-Host "   3.- Suspender servicios"
    Write-Host "   4.- Reiniciar servicios (No inicia los detenidos)."
    Write-Host "   5.- Salir"
    $accion = Read-Host -Prompt "Escoge una opcion"
     switch ($accion){
    1 {
        Iniciar-Serv
        Write-Host `n
        Break
    } 2 {
        Detener-Serv 
        Write-Host `n
        Break
    } 3 {
        Suspender-Serv
        Write-Host `n
        Break
    } 4 {
        Reiniciar-serv
        Write-Host `n
        Break
    } 5 {
        Break
    } default {
        Write-Host "Opcion invalida" `n
    }

}
}
