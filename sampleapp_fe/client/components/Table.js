import React from 'react';
import PropTypes from 'prop-types';
import Tr from './Tr';
import orderedFieldInfo from '../utils/orderedFieldInfo';

const getPropertyValuesInOrder = (property) => {
  const propertyValues = orderedFieldInfo.map(
    fieldInfo => property[fieldInfo.rawName]
  )
  return propertyValues;
}

const Table = ({ properties }) => {
  const labels = orderedFieldInfo.map(fieldInfo => fieldInfo.label);
  const rowValues = properties.map(property => getPropertyValuesInOrder(property));
  const rows = rowValues.map((values, i) => (
    <Tr key={i} values={values}/>
  ))

  return (
    <table>
      <thead>
        <Tr values={labels}/>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  )
}

Table.propTypes = {
  properties: PropTypes.array,
}

export default Table;
