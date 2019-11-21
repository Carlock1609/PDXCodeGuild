const readline = require("readline-sync");

function getCard() {
    let cards = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }
    let userInput = readline.question("Enter in a card: ")
    let card = cards[userInput]
    return card
}
function getHand() {
    let hand = []
    let total = 0

    for(let i = 0; i < 3; i++){
        hand.push(getCard())
        total += hand[i]

        if(total <= 11 && hand[i] === 1) {
            hand.push(10)
        }
        console.log(hand)
    }
    return hand
}
function giveAdvice(hand) {
    let total = 0

    for(let i = 0; i < hand.length; i++) {
        total += hand[i]
    }

    if(total <= 17) {
        console.log(`${total} Hit!`)
    }
    if(total >= 18 && total < 21) {
        console.log(`${total} Stay!`)
    }
    if(total === 21) {
        console.log(`${total} Blackjack!`)
    }
    if(total >= 22) {
        console.log(`${total} Bust!`)
    }
}

function main() {
    console.log("You will be prompted to enter in 3 cards. Then you will recieve advice based on total")
    let hand = getHand()

    giveAdvice(hand)
}
main()