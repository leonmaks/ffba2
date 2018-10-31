import React from "react"

const totalsTable = (props) => {
  return (
    props.dailyTotals.map(entry => (
      <div>{entry}</div>
    ))
  )
}

export default totalsTable
