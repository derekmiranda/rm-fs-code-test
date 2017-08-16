import React from 'react';
import PropTypes from 'prop-types';

const tdStyle = {
  border: '1px solid black',
}

const missingStyle = {
  color: 'gray',
  fontStyle: 'italic',
}

const missing = (
  <span style={missingStyle}>Missing Data</span>
)

const Td = (props) => {
  const { value } = props;
  return (
    <td style={tdStyle}>{ value !== '' ? value : missing }</td>
  )
}

export default Td;
