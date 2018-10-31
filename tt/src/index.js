import React from "react"
import { render } from "react-dom"

class HelloReact extends React.Component {
  render() {
    return(
        <div id='helloReact'>
          Hell_o from react!
        </div>
    )
  }
}

render(<HelloReact />, document.getElementById("root-app"));
