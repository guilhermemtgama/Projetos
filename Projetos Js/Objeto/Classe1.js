class Lancamento{
    constructor(nome = 'Genérico', valor = 0){
        this.nome = nome
        this.valor = valor
    }
}

class CicloFinaceiro{
    constructor(mes, ano){
        this.mes
        this.ano
        this.lancamentos = []
    }

    addLancamentos(...lancamentos) {
        lancamentos.forEach(l => this.lancamentos.push(l))
    }
    
    Sumario(){
        let valorConsolidado = 0
        this.lancamentos.forEach(l => {
            valorConsolidado += l.valor
        })
        return valorConsolidado
    }
}

const Salario  = new Lancamento('Salario',45000)
const contaDeLuz = new Lancamento('luz', -220)
const contas = new CicloFinaceiro(2, 2023)
contas.addLancamentos(Salario, contaDeLuz)
console.log(contas.Sumario())