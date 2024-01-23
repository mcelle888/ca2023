import express, { response } from 'express'
import mongoose from 'mongoose'

const categories = ['Food', 'Gaming', 'Coding', 'Other']

const entries = [
    {categories: 'Food', content: 'Pizza is yummy!'},
    {categories: 'Coding', content: 'Coding is fun!'},
    {categories: 'Gaming', content: 'Skyrim is for the Nords'}
]

mongoose.connect('')
    .then(m =>console.log(m.connection.readyState === 1 ? 'MongoDB connected!': 'MongoDB failed to connect'))
    .catch(err => console.error(err))

const entriesSchema = new mongoose.Schema({
    category: {type: String, required:true},
    content: {type: String, required: true}
})

const EntryModel = mongoose.model('Entry', entriesSchema)


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

app.post('/entries', async (req, res) => {
    try{
    // Get entry data from the request
    // console.log(req.body)
    // Validate (make sure its in the right format)
    // Create a new entry object
    // Push the new entry to the array
    const insertedEntry = await EntryModel.create(req.body)
    // Respond with 201 and the created entry object
    res.status(201).send(insertedEntry)
    }
    catch (err) {
        res.status(400).send({error: err.message})
}
})

app.listen(8001)

