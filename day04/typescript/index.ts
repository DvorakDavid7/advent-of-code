import fs from "fs"


class Card {
    id: string
    matches: number
    copies: number

    constructor(id: string, matches: number, copies: number) {
        this.id = id
        this.matches = matches
        this.copies = copies
    }
}

function isWinning(num: string, reference: string[]): boolean {
    return reference.indexOf(num) !== -1
}

function getCardScore(cardNums: string[], reference: string[]): number {
    let score = 0
    for (const cardNum of cardNums) {
        if (isWinning(cardNum, reference)) {
            if (score === 0) {
                score = 1
                continue
            }
            score *= 2
        }
    }
    return score
}

function getCardMatches(cardNums: string[], reference: string[]): number {
    let matches = 0
    for (const cardNum of cardNums) {
        if (isWinning(cardNum, reference)) {
            matches++
        }
    }
    return matches
}

function updateNumberOfCopies(cards: Card[], startIndex: number, count: number, value: number) {
    for (let i = startIndex; i < startIndex + count; i++) {
        cards[i].copies += value
    }
}

function main() {
    const data = String(fs.readFileSync("./input.txt"))
    const lines = data.split("\n")
    const cards: Card[] = []
    let sum = 0

    for (const line of lines) {
        const [cardInfo, game] = line.split(":")
        const cardId = cardInfo.replace(/\s+/g, " ").trim().split(" ")[1]
        const [left, right] = game.split("|")
        const leftNums = left.split(" ").filter(s => s !== "")
        const rightNums = right.split(" ").filter(s => s !== "")

        const score = getCardScore(leftNums, rightNums)
        const matches = getCardMatches(leftNums, rightNums)

        const card = new Card(cardId, matches, 1)
        cards.push(card)
        sum += score
    }

    for (let i = 0; i < cards.length; i++) {
        const card = cards[i]
        updateNumberOfCopies(cards, i + 1, card.matches, card.copies)
    }
    console.log(sum)
    console.log(cards.map(c => c.copies).reduce((acc, val) => acc + val))
}

main()
