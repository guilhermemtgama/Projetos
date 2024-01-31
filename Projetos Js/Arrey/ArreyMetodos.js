const pilotos = ["Vettel", "Alonso", "Raikkonen", "Massa"]

pilotos.pop() //Massa quebrou o carro!
console.log(pilotos)

pilotos.push("Verstappen")
console.log(pilotos)

pilotos.shift() // Remove o primeiro!
console.log(pilotos)

pilotos.unshift("Hamilton")
console.log(pilotos)

// Splice pode adicionar e remover elementos.

// Adicionar
pilotos.splice(2, 0, "Bottas", "Massa")
console.log(pilotos)

// Remover
pilotos.splice(3,1) // Massa Quebrou =(
console.log(pilotos)

// Slice pega uma parte do Arrey 
const algunsPilotos = pilotos.slice(2)
console.log(algunsPilotos)

const algunsPilotos2 = pilotos.slice(1,4)
console.log(algunsPilotos2)
