import React from 'react'

function HooksDemo() {

    const [count, setCount] = React.useState(0);
    const [color, setColor] = React.useState("red");
    return (
        <>
            <div style={{ color: color }}>
                <hr />
                <h1>Hooks Counter Example</h1>
                Counter Value: {count} <br />
                <button onClick={() => setCount(count + 1)}>Increment</button>
                <button onClick={() => setCount(count - 1)}>Decrement</button>
                <button onClick={() => setCount(0)}>Reset</button>
            </div>
            <hr />
        </>
    )
}

export default HooksDemo
