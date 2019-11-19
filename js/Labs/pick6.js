const readline = require("readline-sync");

// let input = readline.question("enter some text: ")
// console.log(input);

// generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets
function pick6() {
    let winningTicket = [];
    for(let i = 0; winningTicket.length <= 5; i++){
        winningTicket.push(Math.floor((Math.random() * 100) + 1));
    }
    return winningTicket;
}
function ticketGen() {
    randomTicket = [];
    for(let i = 0; randomTicket.length <= 5; i++){
        randomTicket.push(Math.floor((Math.random() * 100) + 1));
    }
    return randomTicket;
}

// which returns the number of matches between the winning numbers and the ticket.
function numMatches(winningTicket, randomTicket) {
    let matches = 0;
    for(let i = 0; i < matches.length; i++){
        if(randomTicket[i] === winningTicket[i]){
            matches += 1
        }
    }
    return matches
}

function tableWin(matches) {
    table = {
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }
    return table.matches
}





function main() {
    let balance = 0
    let number_loops = 50000
    let counter = 0

    while(counter <= number_loops) {
        balance -= 2
        counter += 1

        let getMatches = numMatches(pick6(), ticketGen())
        balance += tableWin(getMatches)
    }
    console.log(balance)
}
main()