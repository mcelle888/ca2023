// const x = 2
// const y = 'dfhd'

function adder(a, b) {
    return a + b
}


async function adderPromise(x, y) {
    if (typeof x === 'number' && typeof y === 'number') {
    const answer = adder (x, y)
    return(answer)
} else {
    throw 'x  and y must be a number'
}
}


adderPromise(10,20)
    .then(value => console.log(value))
    .catch(err => console.error(err))

// to add another digit 
adderPromise(10,20)
    .then(value => {
        adderPromise(value, 100)
            .then(answer => console.log(answer))
    })
    .catch(err => console.error(err))

// alternatively 

async function doStuff(){
const value = await adderPromise(10,20)
console.log(value)
}
    // .then(value => adderPromise(value, 100))
    // .then(answer => console.log(answer))
    // .catch(err => console.error(err))

doStuff()
// adderPromise(112.2,34.1)
// .then(value => alert(value))
// .catch(err => console.error(err))
console.log('Not waiting for resolve!')