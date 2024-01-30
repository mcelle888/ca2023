import React, { useState } from 'react'
import BitcoinIndex from '../BitcoinIndex'



const App = () => {
  let [count, setCount] = useState(0)

  return (
    <>
      <h1>Bitcoin Index</h1>
      <BitcoinIndex />
    </>
  )
}

export default App
