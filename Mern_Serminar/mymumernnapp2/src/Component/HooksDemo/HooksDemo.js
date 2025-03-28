import React from 'react';
import styled from 'styled-components';

// Styled components
const DemoContainer = styled.div`
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
`;

const Title = styled.h1`
  color: ${props => props.color || '#333'};
  text-align: center;
  margin-bottom: 1.5rem;
`;

const CounterDisplay = styled.div`
  font-size: 1.5rem;
  text-align: center;
  margin-bottom: 1.5rem;
  color: ${props => props.color || '#333'};
`;

const ButtonGroup = styled.div`
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
`;

const Button = styled.button`
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  background-color: #3498db;
  color: white;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #2980b9;
  }

  &:active {
    transform: scale(0.98);
  }
`;

const ResetButton = styled(Button)`
  background-color: #e74c3c;

  &:hover {
    background-color: #c0392b;
  }
`;

const Divider = styled.hr`
  border: 0;
  height: 1px;
  background: #eee;
  margin: 2rem 0;
`;

function HooksDemo() {
  const [count, setCount] = React.useState(0);
  const [color, setColor] = React.useState("#3498db"); // Changed default to match button color

  // Change color based on count
  React.useEffect(() => {
    if (count > 0) {
      setColor("#27ae60"); // Green for positive
    } else if (count < 0) {
      setColor("#e74c3c"); // Red for negative
    } else {
      setColor("#3498db"); // Blue for zero
    }
  }, [count]);

  return (
    <DemoContainer>
      <Divider />
      <Title color={color}>Hooks Counter Example</Title>
      
      <CounterDisplay color={color}>
        Counter Value: {count}
      </CounterDisplay>
      
      <ButtonGroup>
        <Button onClick={() => setCount(count + 1)}>Increment</Button>
        <Button onClick={() => setCount(count - 1)}>Decrement</Button>
        <ResetButton onClick={() => setCount(0)}>Reset</ResetButton>
      </ButtonGroup>
      
      <Divider />
    </DemoContainer>
  );
}

export default HooksDemo;