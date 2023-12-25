function bubbleSort(arr) {
    const len = arr.length;

    for (let i = 0; i < len - 1; i++) {
        for (let j = 0; j < len - 1 - i; j++) {
            // Compare adjacent elements
            if (arr[j] > arr[j + 1]) {
                // Swap the elements if they are in the wrong order
                const temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
// unsortedArray is an array of numbers that has not been sorted
const unsortedArray = [64, 34, 25, 12, 22, 11, 90, 80, 90, 300, 55, 21];
const sortedArray = bubbleSort(unsortedArray.slice());

console.log("Unsorted Array:", unsortedArray);
console.log("Sorted Array:", sortedArray);