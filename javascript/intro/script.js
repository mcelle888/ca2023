// let str = 'Hello world!'

// console.log(str.replaceAll('o', '---'))
 

// Python: print(f'Hello, {name}!')

// console.log(`Hello, ${str}!`)
// console.log(`Answer: ${5*10}`)


// console.log(Math.floor(3 / 2))

// let x = 5
// console.log(x)

//Increment X (Python: x += 1)
// x += 1
// x++
// x--

// console.log(x++)
// console.log(x)

// console.log(123 === "123")


// let x = 5
// console.log(typeof x)


// Python: person = {"name": "Michelle"}

// let person = {
//     "name": "Michelle",
//     "age": 27
//     }

// let key = 'name'

// console.log(person[key])


// console.log(person.age)


// x = [1, 2, 3, 3.14159, true, 'hello']

// console.log(x)

// console.log(x[x.length-1])


// python:
// def add(x,y):
//  return x + y 

// function add(x,y) {
//     return x + y
// }


// const Utils = {
//     add: (x,y) =>  x + y,
//     double: x => x * 2,
//     squares: arr => arr.map(x => x ** 2)
// }

// console.log(Utils.add(10, 34))
// // console.log(square(10))

// const numbers = [12, 50, 44, 32, 2]
// const result = Utils.squares(numbers)

// console.log(result)


// DESTRUCTURING

// const people = ['Matt', 'John', 'Mary', 'Kate']

// const [first, second, ...others] = people

// // const first = people[0]
// // const second = people[1]

// console.log(first, second, others)

// const bobBirds = ['Robin', 'Crow']
// const sallyBirds = ['Bluejay', 'Cardinal']

// // const allBirds = bobBirds.concat(sallyBirds)

// const allBirds = [...bobBirds, ...sallyBirds, 'Kookaburra']

// console.log(allBirds)
// //  ... can also break up array into individual elements: in this context, ... is the expansion operator whereas before its used earlier to represent 'rest'
// console.log(...bobBirds)


const me = {name: 'Matt', age: 51, favouriteColor: 'red'}

const me2 = {...me, favouriteColor: 'blue'}

console.log(me)
console.log(me2)