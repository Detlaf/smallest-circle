import React, { Component } from 'react'
import { render } from 'react-dom'
import { Layout, Navbar } from './components'

import { map } from 'lodash'

const Pending = ({ id }) => <h2>Pending: #(id)</h2>
const Result = () => <div />

class Main extends Component {
    constructor(props) {
        super(props)

        this.state = { results: {}, pending: {} }
    }

    render() {
        const { results, pending } = this.state

        return (
            <div className="row">
                <div className="col-xs-6 offset-xs-3">

                </div>
            </div>
        )
    }
}
render(
<Layout main={<Main />} navbar={<Navbar />} />,
        document.getElementById('root')
)