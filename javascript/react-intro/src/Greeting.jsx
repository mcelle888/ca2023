function Greeting({name = 'None', age = 21}) {
  // const  = props
  return (
    <>
      <p>Bonjour, {name}!</p>
      <p>ES: Hola {age}!</p>
    </>
  )
}

export default Greeting