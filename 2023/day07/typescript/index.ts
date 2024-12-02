import fs from "fs"

// card sorted by strength for part 1
const cards1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

// card sorted by strength for part 2
const cards2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

function getFrequencies(cards: string): number[] {
    const freq = new Map<string, number>()
    let maxFreq = 0

    for (const card of cards) {
        const currentFrequency = freq.get(card) || 0;
        const updatedFrequency = currentFrequency + 1
        freq.set(card, updatedFrequency);
        if (updatedFrequency > maxFreq) {
            maxFreq = updatedFrequency
        }
    }
    return Array.from(freq.values()).sort().reverse()
}

function getFrequencyMap(cards: string): Map<string, number> {
    const freq = new Map<string, number>()
    let maxFreq = 0

    for (const card of cards) {
        const currentFrequency = freq.get(card) || 0;
        const updatedFrequency = currentFrequency + 1
        freq.set(card, updatedFrequency);
        if (updatedFrequency > maxFreq) {
            maxFreq = updatedFrequency
        }
    }
    return freq
}

function getMaxHand(hand: string): string {
    const handWithNoJ = hand.replace(/J/g, "")

    if (handWithNoJ === "") {
        return hand.replace(/J/g, "A")
    }

    const freq = getFrequencyMap(handWithNoJ)
    const [maxCard, maxCardFreq] = Array.from(freq.entries()).reduce((max, entry) => (entry[1] > max[1] ? entry : max));
    
    if (maxCardFreq === 1) {
        const max = hand.split("").sort((a, b) => cards2.indexOf(b) - cards2.indexOf(a))[0]
        return hand.replace(/J/g, max)
    }
    return hand.replace(/J/g, maxCard)
}


// comparation function for part 2
function compare2(a: string, b: string): number {
    const maxA = getMaxHand(a)
    const maxB = getMaxHand(b)
    const aFreq = getFrequencies(maxA)
    const bFreq = getFrequencies(maxB)

    if (aFreq.length !== bFreq.length) {
        return bFreq.length - aFreq.length 
    }
    const diff = aFreq[0] - bFreq[0]

    if (diff !== 0) {
        return diff
    }

    // second rule
    for (let i = 0; i < a.length; i++) {
        const aVal = cards2.indexOf(a[i])
        const bVal = cards2.indexOf(b[i])
        if (aVal === bVal) {
            continue
        }
        return aVal - bVal 
    }
    return 0
}


// comparation function for part 1
function compare1(a: string, b: string): number {
    const aFreq = getFrequencies(a)
    const bFreq = getFrequencies(b)

    if (aFreq.length !== bFreq.length) {
        return bFreq.length - aFreq.length 
    }
    const diff = aFreq[0] - bFreq[0]

    if (diff !== 0) {
        return diff
    }

    // second rule
    for (let i = 0; i < a.length; i++) {
        const aVal = cards1.indexOf(a[i])
        const bVal = cards1.indexOf(b[i])
        if (aVal === bVal) {
            continue
        }
        return aVal - bVal 
    }
    return 0
}

function part1(hands: string[], bids: Map<string, number>) {
    hands.sort(compare1)
    const res = Array.from({ length: hands.length }, (_, index) => index + 1)
        .reduce((prev, current, index) => prev + current * (bids.get(hands[index]) || 0), 0)
    console.log(res);
}

function part2(hands: string[], bids: Map<string, number>) {
    hands.sort(compare2)
    const res = Array.from({ length: hands.length }, (_, index) => index + 1)
        .reduce((prev, current, index) => prev + current * (bids.get(hands[index]) || 0), 0)
    console.log(res);
}

function main() {
    const data = String(fs.readFileSync("./input.txt")).split("\n")

    const bids = new Map<string ,number>()
    const hands: string[] = []

    for (const line of data) {
        const [hand, bid] = line.split(" ")
        bids.set(hand, parseInt(bid))
        hands.push(hand)
    }
    part1(hands, bids)
    part2(hands, bids)
}

main()
