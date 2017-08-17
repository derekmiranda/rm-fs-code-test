import React, { Component } from 'react';
import Button from '../components/Button';
import TableContainer from './TableContainer';

const DATA_URL = 'http://localhost:9000/data';

const style = {
  fontFamily: 'sans-serif',
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      properties: [],
      fetchState: '',
    }
    const setStatePromise = (stateChange) => {
      const component = this;
      return new Promise((resolve, reject) => {
        component.setState(stateChange, resolve);
      });
    }

    this._fetchData = async () => {
      await setStatePromise({ fetchState: 'Fetching data...' });
      const res = await fetch(DATA_URL);
      await setStatePromise({ fetchState: '' });
      const properties = await res.json();
      this.setState({
        properties,
      })
    }
  }

  render() {
    const table = this.state.properties.length ?
      <TableContainer properties={this.state.properties} /> :
      null;
    const fetchState = this.state.fetchState && (
      <p>{this.state.fetchState}</p>
    );

    return (
      <main style={style}>
        <h1>California Properties</h1>
        <Button fetchData={this._fetchData} text='Fetch Properties' />
        {fetchState}
        {table}
      </main>
    )
  }
}

export default App;
