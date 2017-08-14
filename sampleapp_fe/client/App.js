import React, { Component } from 'react';
import Button from './Button';
import Table from './Table';

const DATA_URL = 'http://localhost:9000/data';

class App extends Component {
  constructor() {
    super();
    this.state = {
      properties: [],
    }
    this._fetchData = async () => {
      const res = await fetch(DATA_URL);
      const properties = await res.json();
      this.setState({
        properties,
      })
    }
  }

  render() {
    return (
      <main>
        <h1>Properties</h1>
        <Button fetchData={this._fetchData} text='Fetch Properties' />
        <Table properties={this.state.properties} />
      </main>
    )
  }
}

export default App;
