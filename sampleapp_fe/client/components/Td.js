import React from 'react';
import PropTypes from 'prop-types';

const Td = (props) => {
  const { value } = props;
  const tdStyle = {
    border: '1px solid black',
    backgroundColor: value ? 'default' : 'lightgray',
  }
  return (
    <td style={tdStyle}>{value}</td>
  )
}

export default Td;
