export default function getStudentIdsSum(list) {
  const sum = list.reduce((result, item) => result + item.id, 0);
  return sum;
}
