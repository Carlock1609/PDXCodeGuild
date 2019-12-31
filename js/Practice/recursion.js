function blastoff(num) {
    if(num > 0) {
        console.log(num)
        blastoff(num-1)
    }
    else {
        console.log(num)
    }
}
blastoff(3)

function beersonwall(num) {
    part1 = `${num} bottles of beer on the wall, ${num} bottles of beer!\nKnock one down, pass it around, ${num} bottles of beer on the wall!`
    if(num !== -1) {
        console.log(part1)
        beersonwall(num-1)
    }
}
beersonwall(100)
