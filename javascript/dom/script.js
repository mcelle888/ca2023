// const el = document.querySelectorAll('li')
// console.log(el)
// el.innerHTML = 'Hello <span style="color:red">World!</span>'


// const newDiv = document.createElement('div')
// console.log(newDiv)
// document.body.appendChild(newDiv)

// newDiv.innerHTML = '<h3>Awesome content!</h3>'
// newDiv.id = 'spam'
// newDiv.style.color = 'blue'
// document.body.insertBefore(newDiv,document.querySelector('ul'))


// shortened way:

// const myColor = 'blue'
// document.body.innerHTML += `<div id = "spam" style = "color: ${myColor}"> <h3> Awesome content!</h3></div>`

const items = [
'Adding to the DOM',
'Quering the DOM',
'Changing the DOM',
'Event Listeners'
]

const ul = document.querySelector('ul')

// for (let item of items) {
//     // const newLi = document.createElement('li')
//     // newLi.innerText = item
//     // ul.appendChild(newLi)

//     // shorter way of writing above code: 
//     ul.innerHTML += `<li>${item} </li>`
// }

const lis = items.map(item => `<li>${item} </li>`)
console.log(lis.join(''))
ul.innerHTML = lis.join('')

// handle a mouse click on the h1 element

// document.querySelector('h1').addEventListener('click', event => event.target.innerText += '!')

const newItem = document.querySelector('#newItem')
const btn = document.querySelector('button')    



// btn.addEventListener('click',()=> ul.innerHTML += `<li>${newItem.value} </li>`)

btn.addEventListener('click',() => {
ul.innerHTML += `<li>${newItem.value} </li>`
newItem.value = ''
})