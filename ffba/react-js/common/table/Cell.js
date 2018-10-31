import React from "react"
import PropTypes from "prop-types"

const Cell = props => {

  let value_ = null
  let collapse_ = null

  if (!props.hidden && props.value) value_ = props.value

  if (props.collapsible) {
    collapse_ = <span className={
      props.collapse_hide ?
        "fa fa-caret-right ffba-angle-0" :
        "fa fa-caret-down ffba-angle-0"}
    />
  }

  if (props.link) {
    return <td>
      <a href={props.link}>
        {value_} {collapse_}
      </a>
    </td>
  } else
    return <td>{value_} {collapse_}</td>
}

Cell.propTypes = {
  value: PropTypes.node,
  hidden: PropTypes.bool,
  collapsible: PropTypes.bool,
  collapse_hide: PropTypes.bool,
}

export default Cell
