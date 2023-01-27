"use strict";
const n = 3;
// btw range and delay functions were stolen off stack overflow
// imagine skill issue no built in functions for range() L 
const range = (start, end, length = end + 1 - start) => Array.from({ length }, (_, i) => start + i);
function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}
// normal
function towerOfHanoi(n, start = "A", auxiliary = "B", destination = "C") {
    if (n == 1) {
        return console.log(`Disk ${n} moved from ${start} to ${destination}`);
    }
    towerOfHanoi(n - 1, start, auxiliary, destination);
    console.log(`Disk ${n} moved from ${start} to ${destination}`);
    towerOfHanoi(n - 1, start, auxiliary, destination);
}
// towerOfHanoi(n, "B", "A", "C")
// visual (with arrays)
const start = range(1, n).reverse();
const auxiliary = [];
const destination = [];
function towerOfHanoiArrays(n, a, b, c) {
    if (n <= 0) {
        return;
    }
    towerOfHanoiArrays(n - 1, a, c, b);
    let disk = a.pop();
    if (disk)
        b.push(disk);
    console.log(`\n[${start}]\n[${destination}]\n[${auxiliary}]`);
    towerOfHanoiArrays(n - 1, c, b, a);
}
towerOfHanoiArrays(n, start, auxiliary, destination);
