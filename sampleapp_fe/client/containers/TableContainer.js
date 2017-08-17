import React from 'react';
import PropTypes from 'prop-types';
import Table from '../components/Table';
import orderedFieldInfo from '../utils/orderedFieldInfo';
import processProperty from '../utils/processProperty';

const getPropertyValuesInOrder = (property) => {
  const propertyValues = orderedFieldInfo.map(
    fieldInfo => property[fieldInfo.rawName]
  )
  return propertyValues;
}

const TableContainer = ({ properties }) => {
  const labels = orderedFieldInfo.map(fieldInfo => fieldInfo.label);
  const rowValues = properties
    .map(processProperty)
    .map(getPropertyValuesInOrder);

  return <Table rowValues={rowValues} labels={labels}/>
}

TableContainer.propTypes = {
  properties: PropTypes.array,
}

export default TableContainer;
