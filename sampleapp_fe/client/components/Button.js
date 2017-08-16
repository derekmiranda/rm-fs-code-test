import React from 'react';
import PropTypes from 'prop-types';

const Button = (props) => {
  const { fetchData, text } = props;
  return (
    <button onClick={fetchData}>{text}</button>
  )
}

Button.propTypes = {
  fetchData: PropTypes.func,
  text: PropTypes.string,
}

export default Button;
