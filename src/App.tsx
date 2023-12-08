import { Input } from "./ui/input/Input"
// import { Icon } from "./ui/icon/Icon"
import "./scss/style.scss"
import { useState } from "react"


function App() {
    const [value, setValue] = useState("")
    console.log(value)
    
    return (
        <Input 
            placeholder="Username" 
            value={value}
            onChange={setValue}
        />
    )
}
export default App
