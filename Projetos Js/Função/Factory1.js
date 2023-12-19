function criarProduto(nome, preco) {
    return {
        nome,
        preco,
        desconto: 0.1
    }
}

console.log(criarProduto("Notebook", 2119,56))
console.log(criarProduto("IPad", 1150,56))
console.log(criarProduto("Notebook", 3000,56))
console.log(criarProduto("Notebook", 2485,56))