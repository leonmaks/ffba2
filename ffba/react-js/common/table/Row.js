import React, { Component } from "react"
import Auxi from "common/Auxi"
import PropTypes from "prop-types"

import Cell from "common/table/Cell"
import Rows from "common/table/Rows"

class Row extends Component {

  state = {
    hidden: true
  }

  onCollapse = () => {
    this.setState({ hidden: !this.state.hidden })
  }

  render() {

    let tr_ = null
    let group_ = null

    if (!this.props.hidden && this.props.values) {

      const collapsible_ = this.props.group ? true : false

      const values_ = this.props.values.map((v, i) => (
        <Cell key={i}
          value={v.value}
          hidden={v.hidden}
          collapsible={v.collapsible && collapsible_}
          collapse_hide={this.state.hidden}
          link={v.link}
        />
      ))

      tr_ = <tr onClick={collapsible_ ? this.onCollapse : undefined}>{values_}</tr>
    }

    if (this.props.group) {
      group_ = <Rows rows={this.props.group.rows} hidden={this.state.hidden} />
    }

    return (
      <Auxi>
        {tr_}
        {group_}
      </Auxi>
    )
  }
}

Row.propTypes = {
  values: PropTypes.array,
  hidden: PropTypes.bool,
  group: PropTypes.object,
}

export default Row



  // props.values.map((value, i) => {

  //   let html_ = null
  //   if (i === 0 && props.group) {
  //     html_ = (
  //       <td key={i}>
  //         <label htmlFor={value.value}>
  //           {value.value} <span className={props.hidden ? "fa fa-angle-down ffba-angle-0" : "fa fa-angle-up ffba-angle-0"}></span>
  //         </label>
  //       </td>
  //     )
  //   } else
  //     html_ = <td key={i}>{!value.hidden ? value.value : null}</td>

  //   return html_
  // })
