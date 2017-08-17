import processProperty from './processProperty';

describe('processProperty', () => {
  const rawProperty = {
    PROP_NAME: 'named place',
    ADDRESS: '123 place street',
    CITY: 'new yak city',
    STATE_ID: 'ca',
    ZIP: 12345,
  }
  const newProperty = processProperty(rawProperty);

  const checkForFieldCapitalization = (fieldName, fieldLabel, expectedNewField) => {
    it(`should capitalize first letters of ${fieldLabel}`, () => {
      expect(newProperty[fieldName]).toBe(expectedNewField)
    })
  }

  const fieldArgs = [
    ['PROP_NAME', 'property name', 'Named Place'],
    ['ADDRESS', 'address', '123 Place Street'],
    ['CITY', 'city', 'New Yak City'],
  ]
  fieldArgs.forEach((args) => checkForFieldCapitalization(...args));

  it('should change state id to all caps', () => {
    expect(newProperty.STATE_ID).toBe('CA');
  })

  it('should not mutate original property', () => {
    expect(rawProperty).not.toBe(newProperty);
  })
  
})