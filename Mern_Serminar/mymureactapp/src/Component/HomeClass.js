import React from 'react'

class HomeClass extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            name: 'Home'
        }
    }

    render() {
        return (
            <div>
                <h1>Home</h1>
                <p>This is the Home</p>
            </div>
        )
    }
}

export default HomeClass