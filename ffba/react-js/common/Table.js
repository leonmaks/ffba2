import React from "react"

import Headings from "common/table/Headings"
import TBody from "common/table/TBody"

const Table = (props) => {

  let classes_ = "table"
  if (props.classes) classes_ += " " + props.classes

  let headings_ = null
  if (props.headings) headings_ = (
    <thead>
      <tr>
        <Headings headings={props.headings} />
      </tr>
    </thead>
  )

  return (
    <table className={classes_}>
      {headings_}
      <TBody classes={props.classes} rows={props.rows} />
    </table>
  )
}

export default Table
