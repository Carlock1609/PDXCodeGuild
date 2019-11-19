const readline = require("readline-sync");

// let input = readline.question("enter some text: ")
// console.log(input);

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
function numMatches(winningTicket, randomTicket) {
    let matches = 0;
    for(let i = 0; i < randomTicket.length; i++){
        if(randomTicket[i] === winningTicket[i]){
            matches += 1
        }
    }
    return matches
}
function tableWin(matches) {
    table = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000,
    }
    return table[matches]
}

function main() {
    let ticketExpenses = 0
    let earnings = 0
    let number_loops = 100000
    let counter = 0
    let roi = (earnings - ticketExpenses)/ticketExpenses

    while(counter <= number_loops) {
        ticketExpenses -= 2
        counter += 1

        let getMatches = numMatches(pick6(), ticketGen());
        earnings += tableWin(getMatches);

    }
    console.log(`You spent $${ticketExpenses} on tickets.`)
    console.log(`You earned $${earnings}.`)
    // ROI isnt working
    console.log(`Your ROI is $${roi}.`)
}
main()

// (earnings - expenses)/expenses