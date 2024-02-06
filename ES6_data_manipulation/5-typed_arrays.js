export function createInt8TypedArray(length, position, value) {
    if (position < 0 || position >= length){    
        throw new Error('Parameter outside range');
    }
    const int8array = new Int8Array(length);

    const buffer = new ArrayBuffer(length);

    int8array[position] = value;

    return buffer;
        
}
