function fan(){ }
// Armazenar em uma vaviável
const fan1 = function(){ }

const array = [function (a, b) {return a + b}, fan, fan1]
console.log(array[0](2,5))

//Armazenar em um atributo de objeto
const obj = {}

obj.falar = function () {return "Opa"}
console.log(obj.falar())


// passar função como parametro
function run(fun) {
    fun()
}
run (function() {console.log("Executando...")})

// uma função pode retornar/conter uma função
function soma (a, b) { 
     return function(c) {
        console.log(a+b+c)
     }
}

soma(2, 5)(50)