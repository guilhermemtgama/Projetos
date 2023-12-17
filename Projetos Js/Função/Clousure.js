// Clousere é o escopo criado quando uma função é declarada
// Esse escopo permite a funcção acesar e manipular variaveis externas à função

// contexto Lexico em Ação

const x = "Global"

function fora () {
    const x = "Local"
    function dentro(){
        return x
    }
    return dentro
}

const minhaFuncao = fora()
console.log(minhaFuncao())