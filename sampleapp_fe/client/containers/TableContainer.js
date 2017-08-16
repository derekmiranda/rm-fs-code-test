import React from 'react';
import PropTypes from 'prop-types';
import orderedFieldInfo from '../utils/orderedFieldInfo';
import Table from '../components/Table';

const getPropertyValuesInOrder = (property) => {
  const propertyValues = orderedFieldInfo.map(
    fieldInfo => property[fieldInfo.rawName]
  )
  return propertyValues;
}

const TableContainer = ({ properties }) => {
  const labels = orderedFieldInfo.map(fieldInfo => fieldInfo.label);
  const rowValues = properties.map(property => getPropertyValuesInOrder(property));

  return <Table rowValues={rowValues} labels={labels}/>
}

TableContainer.propTypes = {
  properties: PropTypes.array,
}

export default TableContainer;
