import React from 'react';
import { mount } from 'enzyme';
import Table from './Table';
import Tr from '../components/Tr';
import Td from '../components/Td';

const labels = ['Name', 'Address', 'City', 'State', 'Zip Code'];
const properties = [
  ['Mb360 Block11', '701 China Basin', 'San Francisco', 'CA', '94158'],
  ['William Penn Apartment Homes', '2208 W 8th St', 'Los Angeles', 'CA', '90057'],
]
const mountTable = () => {
  return mount(<Table labels={labels} rowValues={properties} />);
}

describe('<Table /> Presentational Component', () => {
  it('should render rows for each property record', () => {
    const mounted = mountTable();
    const tableRows = mounted.find('tbody').find(Tr);
    expect(tableRows.length).toBe(properties.length);
  })

  it('should render cells with correct data', () => {
    const mounted = mountTable();
    const tableRows = mounted.find('tbody').find(Tr);
    
    tableRows.forEach((row, row_i) => {
      const property = properties[row_i];
      property.forEach((value, col_i) => {
        const cell = row.childAt(col_i);
        expect(cell.text().includes(value)).toBe(true);
      })
    })

  })
})