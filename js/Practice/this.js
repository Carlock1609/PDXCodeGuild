let finn = {
    name: "finn",
    sayHi: sayHi,
    bestFriend: {
        name: "Jake the dog",
        age: 38,
        sayHi: sayHi,
    }
}

let lady_rainicorn = {
    name: "lady_unicorn",
    sayHi: sayHi
}

// CAN USE AS MANY THIS LIKE NAME
function sayHi(age, food) {
    console.log(`hello, my name is ${this.name} and i am ${age} years old. and i like to eat ${food}`)
}

// This is how you call object within objects method
console.log(finn.bestFriend.sayHi("3", "dogs"))

// apply spreads your array across your arguements/parameters
// let args1 = [12, "pizza"]
// sayHi.apply(finn, args1)

// let args2 = [1278, "bulgogi"]
// sayHi.apply(lady_rainicorn, args2)


// bind means you if you dont know how many params you have this will be handy
// used for asynchronise coding?
let args1 = [12, "pizza"]
const func1 = sayHi.bind(finn, args1)

let args2 = [1278, "bulgogi"]
const func2 = sayHi.bind(lady_rainicorn, args2)

func1()
func2()