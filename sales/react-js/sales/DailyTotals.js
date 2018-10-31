import React, { Component } from "react"
import axios from "axios"

import Layout from "common/Layout"
import Table from "common/Table"

class DailyTotals extends Component {

  state = {
    totals: [],
  }

  prepareState = (rows) => {

    let sd_ = { ident: null, totals: [0, 0, 0], rows: [] }
    let cr_ = { ident: null, totals: [0, 0, 0], rows: [], link: null }
    let pm_ = { ident: null, totals: [0, 0, 0], rows: [] }

    rows.map((r, i) => {

      if (sd_.ident != r["sales_date"] || cr_.ident != r["cashreg_ident"] || pm_.ident != r["payment"]) {

        // Payment
        if (pm_.ident) {
          pm_.rows.push({
            values: [
              { value: "" },
              { value: "" },
              { value: pm_.ident },
              { value: pm_.totals[0].toFixed(2) },
              { value: pm_.totals[1].toFixed(2) },
              { value: pm_.totals[2].toFixed(2) }
            ],
            key: sd_.ident + "|" + cr_.ident + "!" + pm_.ident
          })
        }
        pm_.ident = r["payment"]
        pm_.totals = [0, 0, 0]
      }

      if (sd_.ident != r["sales_date"] || cr_.ident != r["cashreg_ident"]) {

        // Cashreg
        if (cr_.ident) {
          cr_.rows.push({
            values: [
              { value: "" },
              { value: "", collapsible: true },
              { value: cr_.ident, link: cr_.link },
              { value: cr_.totals[0].toFixed(2) },
              { value: cr_.totals[1].toFixed(2) },
              { value: cr_.totals[2].toFixed(2) }
            ],
            group: { rows: pm_.rows },
            // group: { rows: pm_.rows, hidden: true },
            key: sd_.ident + "|" + cr_.ident
          })
          pm_.rows = []
        }
        cr_.ident = r["cashreg_ident"]
        cr_.link = "/sales/date-cashreg/" + r["sales_date"].replace(/-/g, "/") + "/" + r["cashreg_id"]
        cr_.totals = [0, 0, 0]
      }

      if (sd_.ident != r["sales_date"]) {
        // Sales Date
        if (sd_.ident) {
          sd_.rows.push({
            values: [
              { value: "", collapsible: true },
              { value: "" },
              { value: sd_.ident },
              { value: sd_.totals[0].toFixed(2) },
              { value: sd_.totals[1].toFixed(2) },
              { value: sd_.totals[2].toFixed(2) }
            ],
            group: { rows: cr_.rows },
            // group: { rows: cr_.rows, hidden: true },
            key: sd_.ident
          })
          cr_.rows = []
        }
        sd_.ident = r["sales_date"]
        sd_.totals = [0, 0, 0]
      }

      sd_.totals = [sd_.totals[0] + r["act_sv"], sd_.totals[1] + r["exp_sv"], sd_.totals[2] + r["dis_sv"]]
      cr_.totals = [cr_.totals[0] + r["act_sv"], cr_.totals[1] + r["exp_sv"], cr_.totals[2] + r["dis_sv"]]
      pm_.totals = [pm_.totals[0] + r["act_sv"], pm_.totals[1] + r["exp_sv"], pm_.totals[2] + r["dis_sv"]]
    })

    // Payment (last)
    if (pm_.ident) {
      pm_.rows.push({
        values: [
          { value: "" },
          { value: "" },
          { value: pm_.ident },
          { value: pm_.totals[0].toFixed(2) },
          { value: pm_.totals[1].toFixed(2) },
          { value: pm_.totals[2].toFixed(2) }
        ],
        key: sd_.ident + "|" + cr_.ident + "!" + pm_.ident
      })
    }

    // Cashreg (last)
    if (cr_.ident) {
      cr_.rows.push({
        values: [
          { value: "" },
          { value: "", collapsible: true },
          { value: cr_.ident, link: cr_.link },
          { value: cr_.totals[0].toFixed(2) },
          { value: cr_.totals[1].toFixed(2) },
          { value: cr_.totals[2].toFixed(2) }
        ],
        group: { rows: pm_.rows },
        // group: { rows: pm_.rows, hidden: true },
        key: sd_.ident + "|" + cr_.ident
      })
      pm_.rows = []
    }

    // Sales Date (last)
    if (sd_.ident) {
      sd_.rows.push({
        values: [
          { value: "", collapsible: true },
          { value: "" },
          { value: sd_.ident },
          { value: sd_.totals[0].toFixed(2) },
          { value: sd_.totals[1].toFixed(2) },
          { value: sd_.totals[2].toFixed(2) }
        ],
        group: { rows: cr_.rows },
        // group: { rows: cr_.rows, hidden: true },
        key: sd_.ident
      })
      cr_.rows = []
    }
    return { rows: sd_.rows }
  }

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/sales/daily-totals-for-period-api/").then(
      response => {
        if (response.data.daily_totals) {
          this.setState({ totals: this.prepareState(response.data.daily_totals) })
        }
      }
    )
  }

  render() {

    const data = {
      totals: {
        classes: "table-striped table-sm",
        headings: [
          { name: "", style: { width: "1.4em" } },
          { name: "", style: { width: "1.4em" } },
          { name: "Dimension" },
          { name: "Act.S.V." },
          { name: "Exp.S.V." },
          { name: "Dis.S.V." },
        ],
      }
    }

    return (
      <Layout>
        <div className="table-responsive">
          <Table classes={data.totals.classes} headings={data.totals.headings} rows={this.state.totals.rows} />
        </div>
      </Layout>
    )
  }
}

export default DailyTotals
