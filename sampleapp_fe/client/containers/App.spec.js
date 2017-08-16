import React from 'react';
import { shallow } from 'enzyme';
import App from './App';
import TableContainer from './TableContainer';
import Button from './Button';

describe('<App />', () => {
  it('should render necessary components', () => {
    const wrapper = shallow(<App />);
    expect(wrapper.containsAllMatchingElements([
      <Button />,
      <TableContainer />
    ])).toBe(true)
  })
})