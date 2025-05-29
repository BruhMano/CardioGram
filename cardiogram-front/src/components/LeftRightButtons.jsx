import React from 'react';
import '../assets/static/cards-style.css';

const LeftRightButtons = ({leftFunc, rightFunc}) => {
  return (
      <>
          <div className="screen-left" onClick={leftFunc}></div>
          <div className="screen-right" onClick={rightFunc}></div>
      </>
  );
}

export default LeftRightButtons;