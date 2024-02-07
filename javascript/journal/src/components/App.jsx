import React, { useEffect, useState } from "react"
import Home from "./Home"
import CategorySelection from "./CategorySelection"
import NewEntry from "./NewEntry"
import { BrowserRouter, Route, Routes, useParams } from "react-router-dom"
import NavBar from "./NavBar"
import ShowEntry from "./ShowEntry"

const App = () => {
    const [categories, setCategories] = useState([])
    const [entries, setEntries] = useState([])

    useEffect(() => {
        fetch("http://localhost:8003/categories")
            .then((res) => res.json())
            .then((data) => setCategories(data))

        fetch("http://localhost:8003/entries")
            .then((res) => res.json())
            .then((data) => setEntries(data))
    }, [])

    async function addEntry(cat_id, content) {
        const newId = entries.length
        // 1. Create a entry object from user input
        const newEntry = {
            category: categories[cat_id]._id,
            content: content,
        }
        // POST new entry to API
        const res = await fetch('http://localhost:8003/entries', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newEntry)
        })
        const data = await res.json()
        setEntries([...entries, data])
        // 2. Add new entry to the entries list
        return newId
    }

    // Higher Order Component (HOC)
    function ShowEntryWrapper() {
        const { id } = useParams()
        return <ShowEntry entry={entries[id]} />
    }

    return (
        <>
            <BrowserRouter>
                <NavBar />
                <Routes>
                    <Route path="/" element={<Home entries={entries} />} />
                    <Route path="/category" element={<CategorySelection categories={categories} />} />
                    <Route path="/entry">
                        <Route path=":id" element={<ShowEntryWrapper />} />
                        <Route path="new/:cat_id" element={<NewEntry categories={categories} addEntry={addEntry} />} />
                    </Route>
                    <Route path="*" element={<h3>Page not found</h3>} />
                </Routes>
            </BrowserRouter>
            {/* <Home />
            <CategorySelection />
            <NewEntry /> */}
        </>
    )
}

export default App