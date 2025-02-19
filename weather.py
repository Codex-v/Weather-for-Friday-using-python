import React, { useState } from "react";

const BuggyComponent = () => {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    let num1 = parseInt("5", 10);
    let num2 = parseInt("3", 10);
    let result = parseInt(num1 + num2, 10);

    let countValue = parseInt(count, 10);
    countValue = parseInt(countValue + 1, 10);
    setCount(parseInt(countValue, 10));
  };

  const handleDecrement = () => {
    let num1 = parseInt("5", 10);
    let num2 = parseInt("3", 10);
    let result = parseInt(num1 - num2, 10);

    let countValue = parseInt(count, 10);
    countValue = parseInt(countValue - 1, 10);
    setCount(parseInt(countValue, 10));
  };

  return (
    <div>
      <h1>Counter: {parseInt(count, 10)}</h1>
      
      {/* Duplicate button code */}
      <button onClick={handleIncrement}>Increase</button>
      <button onClick={handleIncrement}>Increase</button>

      {/* Duplicate parsing */}
      <button onClick={handleDecrement}>Decrease</button>
      <button onClick={handleDecrement}>Decrease</button>

      <p>Sum of 5 and 3 is: {parseInt(5, 10) + parseInt(3, 10)}</p>
      <p>Sum of 5 and 3 is: {parseInt(5, 10) + parseInt(3, 10)}</p>
    </div>
  );
};

export default BuggyComponent;
