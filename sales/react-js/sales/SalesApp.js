import React, { Component } from "react"
import { render } from "react-dom"

import DailyTotals from "sales/DailyTotals"

class SalesApp extends Component {
  render() {
    return (
      <DailyTotals />
    )
  }
}

render(<SalesApp />, document.getElementById("sales-app"));
