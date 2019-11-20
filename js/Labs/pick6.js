const readline = require("readline-sync");

function getWinningTic() {
    let winningTicket = [];
    for(let i = 0; i < 6; i++){
        winningTicket.push(Math.floor((Math.random() * 100) + 1));
    }
    return winningTicket;
}
function getRandomTic() {
    let = randomTicket = [];
    for(let i = 0; i < 6; i++){
        randomTicket.push(Math.floor((Math.random() * 100) + 1));
    }
    return randomTicket;
}
function numMatches(winningTicket, randomTicket) {
    let matches = 0;
    for(let i = 0; i < 6; i++){
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

    while(counter < number_loops) {
        ticketExpenses += 2
        counter += 1

        let getMatches = numMatches(getWinningTic(), getRandomTic());
        earnings += tableWin(getMatches);
    }
    console.log(`You spent $${ticketExpenses} on tickets.`)
    console.log(`You earned $${earnings}.`)
    console.log(`Your ROI is $${roi}.`)
}
main()
