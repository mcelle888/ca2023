
import './App.css'
import Greeting from "./Greeting"

function App() {


  return (
    <>
      <h1>Hello</h1>

      <Greeting foo = "bar" name = "Michelle" age = {27} />
      <Greeting abc = "123" name = "Kate" />
      <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolorem recusandae natus, et nesciunt cum quia cumque sunt voluptate odio fugit, corporis temporibus est, inventore facere facilis modi quisquam hic tenetur.</p>
      <Greeting />
    </>

  )
}

export default App
