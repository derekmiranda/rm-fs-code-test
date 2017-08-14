import React from 'react';
import PropTypes from 'prop-types';

const missingStyle = {
  color: 'gray',
}

const missing = (
  <span style={missingStyle}>Missing Data</span>
)

const Td = ({ value }) => (
  <td>{ value !== '' ? value : missing }</td>
)

export default Td;
