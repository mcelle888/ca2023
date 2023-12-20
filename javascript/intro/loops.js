// while loop

// let count = 3 

// while (count > 0) {
//     console.log(count--)
// }


// for loop
// python

// for i in range(10):
//  print(i)


// 3-part for loop
// initialiser runs once, before the first iteration
// condition will be tested before every iteration
// post-iteration executes after every iteration

// for (initialiser; boolean condition; post-iteration) { }




// for (let i = 0; i < 10; i++ ) {
//     console.log(i)
// }

// const numbers = [1, 2, 5, 21, 55, 57]

// for (let i = 0; i < numbers.length; i++ ) {
//     console.log(numbers[i])
// }


// const numbers = [1, 2, 5, 21, 55, 57]

// let res = []
// for (let i = 0, x = 1; i < numbers.length; i++, x +=2 ) {
//     res.push(`${x}. ${numbers[i]}`)
// }

// console.log(res)


// for (let prev=1, next = 1; next <= 1000; tmp=next, next=prev+next, prev=tmp) {
//     console.log(next)
// }

const favFoods = ['pizza', 'pasta', 'tacos']

// Python
// for item in favFoods:
//  print(item)


// for (index of favFoods) {
//     console.log(index)
// }


// for (let index in favFoods) {
//     console.log(`${parseInt(index)+1}. ${favFoods[index]}`)
// }



favFoods.forEach((food, index) => {
    console.log(`${index+1}. ${food}`)
})


favFoods.forEach(food => console.log(food))
