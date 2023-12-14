const valor = "Global"

function minhaFuncao(){
    console.log(valor)
}

function exec(){
    const valor = "local"
    minhaFuncao()
}

exec()