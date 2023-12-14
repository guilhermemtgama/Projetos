function getInteiroAleatorioEntre(min,max){
    const valor = Math.random() * (max-min) + min
    return Math.floor(valor)
}
let opcao = -1

do{
    opcao = getInteiroAleatorioEntre(-1,1000)
    console.log(`Opção esccolhida foi ${opcao}.`)
}while (opcao!= -1)

console.log("fim")