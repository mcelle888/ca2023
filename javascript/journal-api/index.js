import express, { response } from 'express'

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    {categories: 'Food', content: 'Pizza is yummy!'},
    {categories: 'Coding', content: 'Coding is fun!'},
    {categories: 'Gaming', content: 'Skyrim is for the Nords'}
]

const app = express() 

app.use(express.json())

app.get('/', (req, res) => res.send({info: 'Journal API'}))

app.get('/categories', (req, res) => res.send(categories))

app.get('/entries', (req, res) => res.send(entries))

app.get('/entries/:id', (req, res) => {
    const entry = entries[req.params.id - 1]
    if (entry) {
        res.send(entry)
    } else {
        res.status(404).send({error: 'Entry not found'})
    }
})

// post request

app.post('/entries', (req, res) => {
    // Get entry data from the request
    console.log(req.body)
    // Validate (make sure its in the right format)
    // Create a new entry object
    // Push the new entry to the array
    entries.push(req.body)
    // Respond with 201 and the created entry object
    res.status(201).send(entries[entries.length - 1])
})

app.listen(8001)

