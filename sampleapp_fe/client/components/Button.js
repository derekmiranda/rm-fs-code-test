import React from 'react';
import PropTypes from 'prop-types';

const style = {
  fontSize: '1em',
  paddingBottom: '0.5em',
}

const Button = (props) => {
  const { fetchData, text } = props;
  return (
    <button onClick={fetchData} style={style}>{text}</button>
  )
}

Button.propTypes = {
  fetchData: PropTypes.func,
  text: PropTypes.string,
}

export default Button;
