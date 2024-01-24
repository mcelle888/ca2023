import express  from 'express'
import { EntryModel, CategoryModel } from './db.js'

const categories = ['Food', 'Gaming', 'Coding', 'Other']



const app = express() 

app.use(express.json())

app.get('/', (req, res) => res.send({info: 'Journal API'}))

app.get('/categories', async (req, res) => res.send(await CategoryModel.find()))

app.get('/entries', async (req, res) => res.send(await EntryModel.find()))

app.get('/entries/:id', async (req, res) => {
    const entry = await EntryModel.findById(req.params.id)
    console.log(entry)
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


app.put('/entries/:id', async (req, res) => {
    try {
        const updatedEntry = await EntryModel.findByIdAndUpdate(req.params.id, req.body, { new: true})
        if (updatedEntry) {
    res.send(updatedEntry)
        } else {
            res.status(404).send({error: 'Entry not found'})
        }
    }
    catch (err) {
        res.status(400).send({error: err.message})
}
})


app.delete('/entries/:id', async (req, res) => {
    try {
        const deletedEntry = await EntryModel.findByIdAndDelete(req.params.id)
        if (deletedEntry) {
    res.sendStatus(204)
        } else {
            res.status(404).send({error: 'Entry not found'})
        }
    }
    catch (err) {
        res.status(500).send({error: err.message})
}
})


 

app.listen(8002)

