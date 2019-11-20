const readline = require("readline-sync");

function main() {
    let rotation = readline.question("Enter in a rotation: ");
    let encrypt = readline.question("Enter in a msg to be encrypted: ");

    let strLow = "abcdefghijklmnopqrstuvwxyz";
    let strUpp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    let firstHalfLow = strLow.slice(0, rotation % 26);
    let secondHalfLow = strLow.slice(rotation % 26, strLow.length);
    let firstHalfUpp = strUpp.slice(0, rotation % 26);
    let secondHalfUpp = strUpp.slice(rotation % 26, strUpp.length);

    let rotatedLow = `${secondHalfLow}${firstHalfLow}`;
    let rotatedUpp = `${secondHalfUpp}${firstHalfUpp}`;

    let encryptedMSG = "";

    for(let i = 0; i < encrypt.length; i++) {
        if(strLow.includes(encrypt[i])) {
            encryptedMSG += strLow[rotatedLow.indexOf(encrypt[i])];
        };
        if(strUpp.includes(encrypt[i])) {
            encryptedMSG += strUpp[rotatedUpp.indexOf(encrypt[i])];
        };
        if(encrypt[i] === " ") {
            encryptedMSG += " "
        };
    };
    console.log(`Your encrypted message is "${encryptedMSG}"`);
};
main();
