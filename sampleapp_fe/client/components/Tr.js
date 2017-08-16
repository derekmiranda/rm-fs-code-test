import React from 'react';
import PropTypes from 'prop-types';
import Td from './Td';

const Tr = (props) => {
  const { values } = props;
  const cells = values.map(
    (value, i) => <Td key={i} value={value}/>
  );

  return (
    <tr>
      {cells}
    </tr>
  )
}

Tr.propTypes = {
  values: PropTypes.array,
}

export default Tr;
