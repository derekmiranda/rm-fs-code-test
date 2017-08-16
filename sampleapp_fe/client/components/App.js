import React, { Component } from 'react';
import Button from './Button';
import TableContainer from '../containers/TableContainer';
import processProperty from '../utils/processProperty';

const DATA_URL = 'http://localhost:9000/data';

const style = {
  fontFamily: 'sans-serif',
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      properties: [],
    }
    this._fetchData = async () => {
      const res = await fetch(DATA_URL);
      const rawProperties = await res.json();
      const properties = rawProperties.map(processProperty);
      this.setState({
        properties,
      })
    }
  }

  render() {
    const table = this.state.properties.length ?
      <TableContainer properties={this.state.properties} /> :
      null;

    return (
      <main style={style}>
        <h1>Properties</h1>
        <Button fetchData={this._fetchData} text='Fetch Properties' />
        {table}
      </main>
    )
  }
}

export default App;
