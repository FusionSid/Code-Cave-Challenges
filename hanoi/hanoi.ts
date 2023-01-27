const n = 3

// btw range and delay functions were stolen off stack overflow
// imagine skill issue no built in functions for range() L 
const range = (start: number, end: number, length = end + 1 - start) => Array.from({ length }, (_, i) => start + i)
function delay(time: number) {
    return new Promise(resolve => setTimeout(resolve, time));
}


// normal
function towerOfHanoi(n: number, start = "A", auxiliary = "B", destination = "C"): void {
    if (n == 1) {
        return console.log(`Disk ${n} moved from ${start} to ${destination}`)
    }
    towerOfHanoi(n - 1, start, auxiliary, destination)
    console.log(`Disk ${n} moved from ${start} to ${destination}`)
    towerOfHanoi(n - 1, start, auxiliary, destination)
}
towerOfHanoi(n, "B", "A", "C")


// visual (with arrays)
const start: Array<number> = range(1, n).reverse()
const auxiliary: Array<number> = []
const destination: Array<number> = []

function towerOfHanoiArrays(n: number, a: Array<number>, b: Array<number>, c: Array<number>): void {
    if (n <= 0) {
        return
    }
    towerOfHanoiArrays(n - 1, a, c, b)
    let disk = a.pop()
    if (disk) b.push(disk)
    console.log(`\n[${start}]\n[${destination}]\n[${auxiliary}]`)
    towerOfHanoiArrays(n - 1, c, b, a)

}
towerOfHanoiArrays(n, start, auxiliary, destination)