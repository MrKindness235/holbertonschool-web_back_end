export default function getListStudentIds(arrayOfObjects) {
    let result = [];
    if (!Array.isArray((arrayOfObjects))) {
      return result;
    }
    result = arrayOfObjects.map((obj) => obj.id);
    return result;
  }
