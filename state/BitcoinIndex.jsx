import React, { useEffect, useState } from 'react'
import CurrencySelector from './CurrencySelector'

const BitcoinIndex = () => {
  let [price, setPrice] = useState("")
  let [currency, setCurrency] = useState("AUD")

  useEffect(() => {
      fetch(`https://api.coindesk.com/v1/bpi/currentprice/${currency}`)
          .then((res) => res.json())
          .then((data) => setPrice(data.bpi[currency].rate))
  }, [currency])

  return (
      <>
          <CurrencySelector currency={currency} setCurrency={setCurrency} />
          <p>
              Current Price ({currency}): {price}
          </p>
      </>
  )
}

export default BitcoinIndex