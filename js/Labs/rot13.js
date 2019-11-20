const readline = require("readline-sync");
// let input = readline.question("enter some text: ")
// console.log(input);

function main() {
    let encrypt = readline.question("Please enter in a msg to be encrypted: ")

    let str = "abcdefghijklmnopqrstuvwxyz "
    let rot13 = "nopqrstuvwxyzabcdefghijklm "
    let encrypted = ""

    for(let i = 0; i < encrypt.length; i++) {
        encrypted += str[rot13.indexOf(encrypt[i])]
    }

    console.log(`Your encrypted message is "${encrypted}"`)
}
main()