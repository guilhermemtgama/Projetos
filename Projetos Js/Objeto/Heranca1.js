const ferrari = {
    modelo: "f40",
    velMax: 325
}

const volvo = {
    modelo: "V40",
    velMax:280
}

console.log(ferrari.__proto__)
console.log(ferrari.__proto__ === Object.prototype)
console.log(volvo.__proto__ === Object.prototype)
console.log(Object.prototype.__proto__ )


function meuObjeto() {}
console.log(typeof Object, typeof meuObjeto)
console.log(Object.prototype, meuObjeto.prototype)