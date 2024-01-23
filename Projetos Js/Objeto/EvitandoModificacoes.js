// Object.preventExtension
const produto = Object.preventExtensions({
    nome:"Qualquer", preço: 1.99, tag: "promoção"
})
console.log("Extensivel:", Object.isExtensible(produto))

produto.nome= "Borracha"
produto.descricao = "Borracha Branca Escolar"
delete produto.tag
console.log(produto)

//Object.seal
const pessoa = { nome: "Juliana", idade: 24}
Object.seal(pessoa)
console.log("Selado: ", Object.isSealed(pessoa))

pessoa.sobrenome = "Silva"
delete pessoa.nome
pessoa.idade = 50
console.log(pessoa) 