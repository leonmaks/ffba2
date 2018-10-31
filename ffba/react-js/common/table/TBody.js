import React from "react"
import PropTypes from "prop-types"
import Rows from "common/table/Rows"

const Tbody = props => {

  let rows_ = null

  if (!props.hidden && props.rows) {
    rows_ = <Rows rows={props.rows} />
  }

  return (
    <tbody>
      {rows_}
    </tbody>
  )
}

Tbody.propTypes = {
  rows: PropTypes.array,
  hidden: PropTypes.bool,
  // headers: PropTypes.bool,
}

export default Tbody


//   rows_ = (
//     this.props.rows.map((row, i) => {

//       const key_ = this.props.up ? this.props.up + "-" : i

//       let values_ = null
//       let group_ = null

//       if (row.values) {
//         values_ = (
//           <tr>
//             <Entries values={row.values} />
//           </tr>
//         )
//       }

//       // if (row.group) {
//       //   group_ =
//       // }

//       return (
//         <Auxi key={key_}>
//           {values_}
//           {group_}
//         </Auxi>
//       )
//     })
//   )
