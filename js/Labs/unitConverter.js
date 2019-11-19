// Unit Converter
// DONE**

const readline = require("readline-sync");

// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`);

function getFirstUnit(){
    let firstUnit = readline.question("Enter in starting unit (in, ft, yd, m, km, mi): ");
    return firstUnit
}
function getStartUnit(){
    let startingUnit = parseInt(readline.question("Enter in unit length (100, 12, 1.5): "))
    return startingUnit
}
function getSecondUnit(){
    let secondUnit = readline.question("Enter in output unit: ")
    return secondUnit
}

function main(){
    let tableCon = {
        in: 0.0254,
        ft: 0.3048,
        yd: 0.9144,
        m: 1,
        km: 1000,
        mi: 1609.344,
    }

    result = getStartUnit()*(tableCon[getFirstUnit()]/tableCon[getSecondUnit()])
    console.log(`The result is ${result}`)
}
main()

