export default function getListStudents() {
  const Students = [
    {
        firstName: 'Guillaume',
        id: 1,
        location: 'San Francisco',
    },
    {
        firstName: 'James',
        id: 2,
        location: 'Columbia',
    },
    {
        firstName: 'Serena',
        id: 5,
        location: 'San Francisco',
    },
  ];

  let result = [];

  result = Students.map((obj) => ({
    id: obj.id,
    firstName: obj.firstName,
    location: obj.location,
  }));

  return result;
}
