function Aula (nome, VideoID) {
    this.nome = nome
    this.VideoID = VideoID
}

const aula1 = new Aula("Bem Vindo", 123)
const aula2 = new Aula("Até Breve", 456)
console.log(aula1, aula2)

// simulando o new

function novo (f, ...params){
    const obj = {}
    obj.__proto__ = f.prototype
    f.apply(obj, params)
    return obj
}

const aula3 = novo(Aula, "Bem vindo", 123)
const aula4 = novo(Aula, "Até Breve", 456)

console.log(aula4, aula3)