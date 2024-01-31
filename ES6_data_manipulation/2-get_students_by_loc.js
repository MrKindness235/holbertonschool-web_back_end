export default function getStudentsByLocation(list, city) {
    const listByCity = list.filter((student) => student.location === city);
    return listByCity;
  }
