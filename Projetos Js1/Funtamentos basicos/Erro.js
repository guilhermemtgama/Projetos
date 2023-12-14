
function trarErroELAncar(erro){
    throw new Error("Observe a constante Obj...")
}


function imprimirNomeGritando(obj){
    try{
    console.log(obj.name.toUpperCase() + "!!!")
    } catch (e){
        trarErroELAncar(e)
    }finally{
        console.log("Script finalizado")
    }
}

const obj = {nome: "Guilherme"}
imprimirNomeGritando(obj)