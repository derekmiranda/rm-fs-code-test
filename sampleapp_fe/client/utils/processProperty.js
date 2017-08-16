const capitalize = (str) => str.split(' ')
  .map(str => str[0] && str[0].toUpperCase() + str.slice(1))
  .join(' ')

export default (property) => {
  const newProperty = Object.assign(property, {
    PROP_NAME: capitalize(property.PROP_NAME),
    ADDRESS: capitalize(property.ADDRESS),
    CITY: capitalize(property.CITY),
    STATE_ID: property.STATE_ID.toUpperCase(),
  });
  return newProperty;
}