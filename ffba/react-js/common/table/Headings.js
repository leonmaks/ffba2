import React from "react"

const Headings = (props) => (
  props.headings.map((heading, i) => {
    if (heading.style) {
      return <th key={i} style={heading.style}>{heading.name}</th>
    }
    return <th key={i}>{heading.name}</th>
  })
)


// const Cell = props => {

//   let value_ = null
//   let collapse_ = null
//   // let style_ = null

//   if (!props.hidden && props.value) value_ = props.value

//   if (props.collapsible) {
//     collapse_ = <span className={
//       props.collapse_hide ?
//         "fa fa-plus ffba-angle-0" :
//         "fa fa-minus ffba-angle-0"}
//     />

//     // style_ = 'style="width: 5em"'
//   }

//   return <td>{value_} {collapse_}</td>
// }





export default Headings
