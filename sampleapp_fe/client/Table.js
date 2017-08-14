import React from 'react';
import PropTypes from 'prop-types';

const Table = ({ properties }) => {
  return (
    <ul>{
    properties.map((property, i) => (
      <li key={i}>{JSON.stringify(property)}</li>
      ))
    }</ul>
  )
}

Table.propTypes = {
  properties: PropTypes.array,
}

export default Table;
