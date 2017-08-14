import React, { Component } from 'react';
import Button from './Button';

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
        <h1>Hello World!</h1>
        <Button fetchData={this._fetchData} text='Fetch Properties' />
        <ul>{this.state.properties && 
          this.state.properties.map((property, i) => <li key={i}>{JSON.stringify(property)}</li>)
        }</ul>
      </main>
    )
  }
}

export default App;
