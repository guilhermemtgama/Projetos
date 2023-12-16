function soBoanoticia(nota){
    if(nota >= 7){
        console.log("Aprovado " + nota)
    }
}

function seForVerdadeEuFalo(Valor){
    if(Valor){
        console.log("É verdade..." + Valor)
    }
}

soBoanoticia(8.1)
soBoanoticia(6.4)

seForVerdadeEuFalo()
seForVerdadeEuFalo(null)
seForVerdadeEuFalo(undefined)
seForVerdadeEuFalo(NaN)
seForVerdadeEuFalo('')
seForVerdadeEuFalo(0)
seForVerdadeEuFalo(-1)
seForVerdadeEuFalo(' ')
seForVerdadeEuFalo("?")
seForVerdadeEuFalo([])
seForVerdadeEuFalo([1, 2])
seForVerdadeEuFalo({})