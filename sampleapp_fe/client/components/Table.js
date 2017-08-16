import React from 'react';
import PropTypes from 'prop-types';
import Tr from './Tr';

const style = {
  border: '1px solid black',
}

const headerStyle = {
  backgroundColor: 'powderblue',
}

const Table = (props) => {
  const { labels, rowValues } = props;
  const rows = rowValues.map((values, i) => {
    return (
      <Tr key={i} values={values}/>
    )
  })

  return (
    <table style={style}>
      <thead style={headerStyle}>
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
